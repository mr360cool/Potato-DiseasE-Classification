# Deployment

This repository is a React frontend and FastAPI API. Deploy both services on
Render; it is not a Streamlit application.

## 1. Deploy the API on Render

1. In Render, choose **New > Blueprint** and connect this GitHub repository.
2. Render reads `render.yaml` and creates the `potato-disease-api` web service.
3. After deployment, copy the service URL, such as
   `https://potato-disease-api.onrender.com`.

The API loads `saved_model/1.keras` from the repository and serves predictions
at `/predict`. Its health endpoint is `/ping`.

## 2. Deploy the frontend on Render

1. In Render, choose **New > Static Site** and enter the public GitHub
   repository URL.
2. Set **Root Directory** to `Frontend`, **Build Command** to
   `npm ci && npm run build`, and **Publish Directory** to `build`.
3. Add `REACT_APP_API_URL` with the API URL copied from Render followed by
   `/predict` (for example,
   `https://potato-disease-api-6xpk.onrender.com/predict`).
4. Deploy. The live site URL shown by Render is the frontend link to share.
5. Set the API service's `FRONTEND_ORIGINS` to that frontend URL's origin
   (without a trailing slash) and redeploy the API.

The frontend API URL is embedded at build time. If you change it later, redeploy
the frontend. Render's free web services may take a short time to wake after
being idle. Public Git repository deployments do not automatically redeploy
when code changes; trigger a manual deploy from Render after pushing updates.
