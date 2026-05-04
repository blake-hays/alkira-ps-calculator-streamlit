# Alkira PS Quote / SOW Calculator — Streamlit

Streamlit port of the [PS-Quote-Calculator-SOW-](https://github.com/dsh4757/PS-Quote-Calculator-SOW-) HTML app. Same service catalog (29 services across 5 categories), same S/M/L/XL/Custom sizing, same Quote and SOW outputs.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Community Cloud

1. Push `app.py` and `requirements.txt` to a new GitHub repo.
2. Go to https://share.streamlit.io, **New app**, point at the repo, set the main file to `app.py`.
3. Deploy. The default `streamlit` runtime is enough — no secrets needed.

## What's in here

- `app.py` — single-file Streamlit app
- `requirements.txt` — pins Streamlit
- Service catalog, sizing, deliverables, and SOW boilerplate live inside `app.py`. Edit there to change copy.

## Tabs

- **Calculator** — pick services, sizes, see live total
- **Quote** — formatted quote with cost breakdown, plus `.txt` download
- **SOW** — full Statement of Work with executive summary, scope, terms, assumptions, signature block; downloads as `.md`

Customer + partner details and the hourly rate live in the sidebar so they apply to both Quote and SOW.
