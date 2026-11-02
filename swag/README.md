# Corporate swag order pages

One folder per client. Employees pick items within a points budget, add their name, and Submit opens a pre-filled Microsoft Form; responses collect in an Excel file the client supervisor can view.

- `american-track/`: live at https://licatja.github.io/smoky-woods-assets/swag/american-track/ once merged to main.
- `_build/`: `prep.py` resizes mockups from the project files into `img/`; `build.py [form-link]` writes `index.html` (and a preview with inlined images). Item list, points and colors live in the ITEMS block of `template.html`.
