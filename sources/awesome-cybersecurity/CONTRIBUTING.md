# Contributing

Let's grow this list together. Please read the rules below before adding a resource or sending a fix.

🇹🇷 [Türkçe katkı rehberi](CONTRIBUTING.tr.md)

## Inclusion Criteria

A resource can be added if it is:

1. **Active and reliable**: updated within the last 12 months, or an established reference.
2. **Legal and ethical**: pirated content, leaked courses, cracks and sites that distribute malware are **not accepted**.
3. **In the right category**. If it fits several domains, it may be added to each relevant section.
4. **Marked with a price badge**:
   - 🟢 Free
   - 🟡 Freemium (free tier + paid)
   - 🔴 Paid
5. **Marked with a Side / Role badge**:
   - ⚔️ Offensive: Pentest, Web, Bug Bounty, Red Team, Exploit/RE, Mobile, API, Cloud, AI Red Team, CTF
   - 🛡️ Defensive: SOC, DFIR, Detection, Malware Analysis, AppSec, Vuln Mgmt, Hardening, Threat Intel, Cloud Security
   - ⚔️🛡️ Mixed: resources with both offensive and defensive content (Purple Team)
   - 🏛️ GRC: governance, risk and compliance
   - 🧩 Shared: fundamentals, cryptography, standards, news and general resources

   Pick the badge by the resource's **main content**. If unsure, say so in the PR description.
6. **Free of ads and affiliate links**: use the official URL.

## Languages and Files

The list is maintained in two files: **README.md** (English) and **OKUBENI.md** (Turkish). Add your resource to both, in the same section and the same table. If you cannot write one of the languages, say so in the PR description and a maintainer will complete it.

## Row Format

Each section has two tables: **🟢 Free** and **💳 Paid**. Fully free resources (🟢) go in the first table; resources with a free tier (🟡) or paid ones (🔴) go in the second. Tables list resources only: do not add "start here" style learning paths or ranking advice.

Keep the column order. Example:

```markdown
| [Resource Name](https://example.com) | ⚔️ Pentest | Type | 🟡 | Beginner | One neutral sentence |
```

Column order: **Resource · Side / Role · Type · Price · Level · Notes**. (Some tables have no Type or Level column; follow the existing columns of that section.)

- Keep the current ordering of each table.
- Keep the note to one sentence and avoid marketing language.
- Do not write exact prices (they change); the badge is enough.

## Pull Request Checklist

- [ ] The link works and points to the official source
- [ ] The price badge is correct
- [ ] The Side / Role badge is correct
- [ ] The type and level are correct
- [ ] It is in the right section and table, in the same format
- [ ] The resource is not already in the list
- [ ] The resource was added to both README.md and OKUBENI.md
- [ ] If the resource count changed, the `resources` badge in both files was updated

## Updates and Fixes

If a price, plan or certification name changed, open a PR and include the official page link as the source in the PR description.

## Link Checking

The repo includes a GitHub Actions workflow (`.github/workflows/link-check.yml`) that checks links weekly and on every PR. You can report broken links as issues or send a fix PR directly.

## Local Check

Before opening a PR, run `python scripts/validate.py` (Python 3, no dependencies). It verifies that `README.md` and `OKUBENI.md` list the same resources, that tables are well-formed, that in-page links work and that the `resources` badge is correct. The same check runs automatically on every PR.

You can also suggest a resource or report a broken link with the [issue templates](https://github.com/cveburak/awesome-cybersecurity/issues/new/choose).

## Conduct

Be respectful. No personal attacks and no disparaging competing resources. See the [Code of Conduct](.github/CODE_OF_CONDUCT.md).
