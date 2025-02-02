# Detailed Guide for Translation Contributors

## What is GitHub?

GitHub is a website that helps people collaborate on software projects and documents. Think of it like Google Docs for code and technical documents, but with more powerful features for tracking changes and managing different versions. You don't need to be a programmer to contribute translations - you'll just be editing text files!

## Creating a GitHub Account

1. Go to [github.com](https://github.com)
2. Click the "Sign up" button in the top-right corner
3. Follow the registration process:
   - Enter your email address
   - Create a password
   - Choose a username
   - Complete any verification steps

## Finding Your Language Branch

1. Go to the [AI Nutshell repository](https://github.com/hkniberg/ainutshell)
2. Click the dropdown menu that says "preview" (near the top of the page)
3. In the branch list, look for `preview-xx` where `xx` is your language code. If you don't know the language code, see [this list of language codes](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes).
   - For example, `preview-ja` for Japanese
   - `preview-es` for Spanish
   - `preview-fr` for French
   - etc.

## Option 1: Editing Directly in GitHub (Easiest Method)

This is the simplest way to contribute, as it requires no software installation:

1. After finding your language branch, navigate to the `manuscript` folder
2. Click on `manuscript.md` (this contains the main book content)
3. Click the pencil icon (🖊️) in the top-right corner of the file view
4. It will ask if you want to fork the repository. Click "Fork". That basically makes a copy of the repository under your GitHub account.
5. Make your translation improvements directly in the editor
6. When you're done editing:
   - Scroll to the bottom of the page
   - Add a brief description of your changes in the "Commit changes" box
   - Select "Create a new branch for this commit and start a pull request"
   - Click "Propose changes"
7. On the next screen, click "Create pull request"

You can also edit `metadata.md` the same way if you want to improve the translation of the title, subtitle, or back cover text.

## Option 2: Editing Locally on Your Computer

If you prefer to edit the files using your own text editor:

1. After finding your language branch, navigate to the `manuscript` folder
2. For each file you want to edit:
   - Click on the file (`manuscript.md` or `metadata.md`)
   - Click the "Raw" button (near the top right of the file view)
   - Right-click anywhere in the text and select "Save As" (or press Ctrl+S / Cmd+S)
   - Save the file to a folder on your computer
3. Edit the files using any text editor you prefer (Notepad, TextEdit, VS Code, etc.)
4. When you're done editing:
   - Go back to GitHub
   - Navigate to your language branch and the file you edited
   - Click the pencil icon
   - Copy and paste your edited content from your local file
   - Scroll to the bottom of the page
   - Add a brief description of your changes in the "Commit changes" box
   - Select "Create a new branch for this commit and start a pull request"
   - Click "Propose changes"
5. On the next screen, click "Create pull request"

## Important Tips

- Always check the original English text (in the `publish` branch) if something is unclear
- Don't change the special tags like `{i: "word"}` or `{alt: "text"}`
- Keep the same informal tone and style as the original
- Only fix what needs fixing - don't rewrite everything
- You can edit multiple times - each change will update your pull request automatically
- If you need help, you can create an "Issue" on GitHub or email ainutshell@ymnig.ai

## What Happens After Your Pull Request

1. The author and his AI assistant will review your changes
2. If everything looks good, they'll approve and merge your changes
3. The ebook version will be updated on Leanpub
4. The Amazon version will be updated in the next quarterly update

Thank you for helping improve the translations! 🙏
