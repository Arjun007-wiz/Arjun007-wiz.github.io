# Arjun007-wiz.github.io — Static personal site

This repository holds a small static website scaffold generated from `design.md`.

What I added
- `index.html` — home/landing page
- `about.html` — editable About Me page (update with your bio)
- `quiz.html` + `scripts/quiz.js` — a simple quiz that uses answers matching the About page
- `styles/styles.css` — simple responsive stylesheet

How to view locally
1. Open `index.html` in your browser, or run a simple static server (recommended):

```powershell
# using Python 3 (Windows PowerShell)
python -m http.server 8000; Start-Process http://localhost:8000
```

2. Edit `about.html` to update content. Then update `scripts/quiz.js` answers to match the About page.

Deploy to GitHub Pages
1. Push to the `main` branch of this repository.
2. In the repository Settings on GitHub, go to Pages and select the `main` branch (root) as the source.
3. Save and wait a minute — your site will be available at `https://<your-username>.github.io/<repo-name>/`.

Next steps / optional
- Replace placeholder bio and quiz answers.
- Add images under `assets/` and reference them in `about.html`.
- Add more pages (projects, contact form) or a theme.
