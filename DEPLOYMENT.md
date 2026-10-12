# Deployment

This repository is a React frontend and FastAPI API. Deploy the API on Render
and the frontend on Vercel; it is not a Streamlit application.

## 1. Deploy the API on Render

1. In Render, choose **New > Blueprint** and connect this GitHub repository.
2. Render reads `render.yaml` and creates the `potato-disease-api` web service.
3. After deployment, copy the service URL, such as
   `https://potato-disease-api.onrender.com`.
4. In the Render service's environment settings, set `FRONTEND_ORIGINS` to the
   production Vercel site origin (for example,
   `https://potato-disease-classifier.vercel.app`, without a trailing slash),
   then redeploy the API.

The API loads `saved_model/1.keras` from the repository and serves predictions
at `/predict`. Its health endpoint is `/ping`.

## 2. Deploy the frontend on Vercel

1. In Vercel, import this GitHub repository.
2. Set **Root Directory** to `Frontend`.
3. Add the environment variable `REACT_APP_API_URL` with the API URL copied
   from Render followed by `/predict` (for example,
   `https://potato-disease-api.onrender.com/predict`).
4. Deploy. The live site URL shown by Vercel is the frontend link to share.

The frontend API URL is embedded at build time. If you change it later, redeploy
the frontend. Render's free web services may take a short time to wake after
being idle.
