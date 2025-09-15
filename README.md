# Real‑Time eSSVI Surface (SPX / Polygon)

**Arbitrage‑aware eSSVI fit on live Polygon SPX option chains** with diagnostics
(θ(T), ρ(T), ψ(T), φ(T)), Δ–T heatmaps, RR/BF tables, and interactive Plotly surfaces.
Designed to be recruiter‑friendly: clear metrics, visuals, and reproducible steps.

<p align="center">
  <img src="docs/preview.png" alt="preview" width="640"/>
</p>

## Highlights
- Pulls **vendor IV** from Polygon for SPX (I:SPX) and uses **Yahoo (^GSPC)** for spot.
- Filters strikes by a *previous filter* around snapshot spot to ensure stability.
- Fits **eSSVI** per expiry with smoothness regularization; enforces G&J bound softly.
- Produces:
  - Parameter curves: θ(T), ρ(T), ψ(T), φ(T)
  - Model vs vendor IV scatter, residual histogram
  - **Δ–T heatmap**, **RR/BF 25Δ table**, and **3D surfaces (IV / w)** with HTML exports
- Saves artifacts into `plots/` (HTML + PNG if `kaleido` installed).

> **Metric:** Example run MAE ≈ **30 bps** of IV (sample day; may vary by market).

## Quickstart

```bash
git clone <YOUR-REPO-URL>.git
cd realtime-essvi-surface
python -m venv .venv && source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Set your Polygon key (recommended via `.env`):

```
POLYGON_API_KEY=YOUR_KEY_HERE
```

### Option A — Notebook
Open **`notebooks/real_time_fit.ipynb`**, run all cells. Artifacts will appear in **`plots/`**.

### Option B — CLI wrapper (executes the notebook)
```bash
python -m src.realtime_essvi.run_notebook
```

> The CLI uses `jupyter nbconvert` to execute the notebook in place.

## Repo Layout
```
realtime-essvi-surface/
├── notebooks/
│   └── real_time_fit.ipynb        # main pipeline (provided)
├── src/realtime_essvi/
│   ├── __init__.py
│   └── run_notebook.py            # optional wrapper to execute the notebook
├── plots/                         # outputs (HTML/PNG) — gitignored
├── examples/                      # sample data (optional)
├── docs/
│   └── preview.png                # put a screenshot for README
├── requirements.txt
├── .gitignore
├── LICENSE (MIT)
└── README.md
```

## Notes
- Static PNG export requires `kaleido` (already in `requirements.txt`).
- Do **not** commit secrets. `.env` is git‑ignored; use `.env.example` as a template.
- If you have an older SSV/vol repo, keep it public but **archive it** and link here.

## Citation
If this code helps you, please star the repo. Feel free to reference:
> Karayel, F. (2025). *Real‑Time eSSVI Surface (SPX / Polygon)*. GitHub repository.

## License
MIT — see `LICENSE`.
