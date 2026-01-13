This is the technical version of the source code for the book "Generative AI in a Nutshell - How to Survive and Thrive in the Age of AI". The structure is optimized for publishing on leanpub.

# Translations

Translations are maintained in the [ainutshell-translations](https://github.com/hkniberg/ainutshell-translations) repo, which is designed to be translator-friendly (no branches, simple structure).

## Importing translations

To import a translation from ainutshell-translations:

```bash
python scripts/import-translation.py <lang>
```

For example, to import the Danish translation:

```bash
python scripts/import-translation.py da
```

This will:
1. Checkout the `preview-da` branch and pull latest
2. Copy `manuscript-da.md` → `manuscript/manuscript.md`
3. Copy `metadata-da.md` → `manuscript/metadata.md`
4. If translated images exist in `resources-da/`, copy them to `resources/` with corrected names and update image references
5. Offer to commit the changes

After committing, push to trigger Leanpub preview generation. Once verified, create a PR from `preview-<lang>` to `publish-<lang>`.

# Branch structure

- preview: English version of the book, pushing here will cause a new preview version to be generated on Leanpub
- publish: English verrsion of the book, pushing here will cause the published version to be updated on Leanpub
- preview-<language>: version of the book in <language>, pushing here will cause a new preview version to be generated on Leanpub
- publish-<language>: version of the book in <language>, pushing here will cause the published version to be updated on Leanpub

# Available translations

- ar (Arabic)
- bs (Bosnian)
- cs (Czech)
- da (Danish)
- de (German)
- el (Greek)
- es (Spanish)
- fr (French)
- he (Hebrew)
- hi (Hindi)
- hr (Croatian)
- hu (Hungarian)
- id (Indonesian)
- it (Italian)
- ja (Japanese)
- ko (Korean)
- nb (Norwegian Bokmål)
- nl (Dutch)
- pa (Punjabi)
- pl (Polish)
- pt-BR (Portuguese - Brazil)
- pt-PT (Portuguese - Portugal)
- ro (Romanian)
- sr-Latn (Serbian Latin)
- sv (Swedish)
- th (Thai)
- tr (Turkish)
- uk (Ukrainian)
- vi (Vietnamese)
- zh-Hans (Chinese Simplified)
- zh-Hant (Chinese Traditional)
