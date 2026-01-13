#!/usr/bin/env python3
"""
Import a translation from ainutshell-translations repo to ainutshell repo.

This script:
1. Checks out the preview-<lang> branch in ainutshell
2. Copies manuscript and metadata from ainutshell-translations
3. Handles translated images if they exist
4. Offers to commit the changes

Usage:
    python scripts/import-translation.py <language-code>
    
Example:
    python scripts/import-translation.py da
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


def run_cmd(cmd, cwd=None, check=True):
    """Run a shell command and return output."""
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=check)
    return result.stdout.strip()


def has_uncommitted_changes(repo_path):
    """Check if repo has uncommitted changes."""
    status = run_cmd(["git", "status", "--porcelain"], cwd=repo_path)
    return bool(status)


def get_current_branch(repo_path):
    """Get current git branch."""
    return run_cmd(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repo_path)


def main():
    parser = argparse.ArgumentParser(description="Import translation from ainutshell-translations")
    parser.add_argument("lang", help="Language code (e.g., 'da' for Danish)")
    args = parser.parse_args()
    
    lang = args.lang
    
    # Determine repo paths (assume sibling directories)
    script_dir = Path(__file__).resolve().parent
    ainutshell_repo = script_dir.parent
    translations_repo = ainutshell_repo.parent / "ainutshell-translations"
    
    print(f"ainutshell repo: {ainutshell_repo}")
    print(f"translations repo: {translations_repo}")
    print()
    
    # Validate repos exist
    if not (ainutshell_repo / ".git").exists():
        print(f"Error: {ainutshell_repo} is not a git repository")
        sys.exit(1)
    
    if not translations_repo.exists():
        print(f"Error: Translations repo not found at {translations_repo}")
        sys.exit(1)
    
    # Validate translation files exist
    manuscript_src = translations_repo / "manuscript" / f"manuscript-{lang}.md"
    metadata_src = translations_repo / "metadata" / f"metadata-{lang}.md"
    resources_src = translations_repo / "manuscript" / f"resources-{lang}"
    
    if not manuscript_src.exists():
        print(f"Error: Manuscript not found: {manuscript_src}")
        sys.exit(1)
    
    if not metadata_src.exists():
        print(f"Error: Metadata not found: {metadata_src}")
        sys.exit(1)
    
    # Check for uncommitted changes
    if has_uncommitted_changes(ainutshell_repo):
        print("Error: ainutshell repo has uncommitted changes. Please commit or stash them first.")
        sys.exit(1)
    
    # Remember current branch to return to it if something fails
    original_branch = get_current_branch(ainutshell_repo)
    preview_branch = f"preview-{lang}"
    
    print(f"Importing {lang} translation...")
    print()
    
    try:
        # Pull latest translations
        print("Pulling latest from ainutshell-translations...")
        run_cmd(["git", "pull"], cwd=translations_repo)
        
        # Checkout preview branch
        print(f"Checking out {preview_branch}...")
        run_cmd(["git", "checkout", preview_branch], cwd=ainutshell_repo)
        run_cmd(["git", "pull"], cwd=ainutshell_repo)
        
        # Copy manuscript
        manuscript_dst = ainutshell_repo / "manuscript" / "manuscript.md"
        print(f"Copying manuscript...")
        shutil.copy2(manuscript_src, manuscript_dst)
        
        # Copy metadata
        metadata_dst = ainutshell_repo / "manuscript" / "metadata.md"
        print(f"Copying metadata...")
        shutil.copy2(metadata_src, metadata_dst)
        
        # Handle translated images if they exist
        if resources_src.exists() and resources_src.is_dir():
            print(f"Processing translated images from {resources_src.name}...")
            resources_dst = ainutshell_repo / "manuscript" / "resources"
            
            # Build a mapping of old filename -> new filename for manuscript updates
            image_renames = {}  # old_name -> new_name
            image_count = 0
            
            for image_file in resources_src.iterdir():
                if image_file.is_file():
                    old_name = image_file.name
                    stem = image_file.stem  # filename without extension
                    ext = image_file.suffix  # .png, .jpg, etc.
                    
                    # Remove -<lang> suffix if present
                    # Supports both: "020-roles-da.jpg" and "020-roles.jpg"
                    lang_suffix = f"-{lang}"
                    if stem.endswith(lang_suffix):
                        new_stem = stem[:-len(lang_suffix)]
                        new_name = f"{new_stem}{ext}"
                    else:
                        # No language suffix - use filename as-is
                        new_name = old_name
                    
                    dst_path = resources_dst / new_name
                    shutil.copy2(image_file, dst_path)
                    
                    if old_name != new_name:
                        print(f"  {old_name} -> {new_name}")
                    else:
                        print(f"  {old_name}")
                    
                    image_renames[old_name] = new_name
                    image_count += 1
            
            print(f"Copied {image_count} translated images")
            
            # Update image references in manuscript
            print("Updating image references in manuscript...")
            with open(manuscript_dst, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Replace all references from resources-<lang>/ to resources/
            # This handles both naming conventions:
            #   (resources-da/020-roles-da.jpg) -> (resources/020-roles.jpg)
            #   (resources-da/020-roles.jpg) -> (resources/020-roles.jpg)
            update_count = 0
            new_content = content
            
            for old_name, new_name in image_renames.items():
                old_ref = f"resources-{lang}/{old_name}"
                new_ref = f"resources/{new_name}"
                if old_ref in new_content:
                    new_content = new_content.replace(old_ref, new_ref)
                    update_count += new_content.count(new_ref) - content.count(new_ref)
            
            # Also handle any remaining resources-<lang>/ references not in our rename map
            # (in case manuscript references images that weren't in the translated folder)
            pattern = rf'resources-{lang}/'
            remaining_matches = len(re.findall(pattern, new_content))
            if remaining_matches > 0:
                print(f"  Warning: {remaining_matches} references to resources-{lang}/ not matched to translated images")
            
            if new_content != content:
                with open(manuscript_dst, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated image references")
            else:
                print("No image references needed updating")
        else:
            print(f"No translated images folder found (checked for {resources_src.name})")
        
        print()
        print("=" * 60)
        print("Import complete!")
        print("=" * 60)
        print()
        
        # Show git status
        print("Changes made:")
        status = run_cmd(["git", "status", "--short"], cwd=ainutshell_repo)
        print(status)
        print()
        
        # Suggest commit message
        commit_msg = f"Import {lang} translation from ainutshell-translations"
        print(f"Suggested commit message: {commit_msg}")
        print()
        
        # Offer to commit
        response = input("Would you like to commit these changes? [y/N] ").strip().lower()
        if response == "y":
            run_cmd(["git", "add", "."], cwd=ainutshell_repo)
            run_cmd(["git", "commit", "-m", commit_msg], cwd=ainutshell_repo)
            print("Changes committed!")
            print()
            print("Next steps:")
            print(f"  1. Push: git push origin {preview_branch}")
            print("  2. Wait for Leanpub to generate preview PDF")
            print("  3. Review the PDF")
            print(f"  4. If OK, create PR from {preview_branch} to publish-{lang}")
        else:
            print("Changes not committed. You can commit manually when ready.")
            print()
            print(f"  git add .")
            print(f"  git commit -m \"{commit_msg}\"")
            print(f"  git push origin {preview_branch}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        
        # Try to return to original branch
        try:
            run_cmd(["git", "checkout", original_branch], cwd=ainutshell_repo, check=False)
        except:
            pass
        
        sys.exit(1)


if __name__ == "__main__":
    main()
