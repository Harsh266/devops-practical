# Principles-of-DevOps-and-Web-API-Development

## Q5: Deploying on Render

### `requirements.txt`

```text
fastapi
uvicorn
pytest
httpx
```

### Render commands

- **Runtime:** Python 3
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `uvicorn app:app --host 0.0.0.0 --port $PORT`

The `$PORT` environment variable is provided by Render and allows the service
to listen on the port assigned to it.

### Creating the Render web service

1. Sign in to Render and select **New > Web Service**.
2. Connect the GitHub account and select the repository containing this app.
3. Select the repository branch to deploy.
4. Select **Python 3** as the runtime.
5. Enter the build and start commands shown above.
6. Add the environment variable `APP_ENV=production`.
7. Select **Create Web Service** and wait for the deployment to finish.

After deployment, replace `<your-render-service-url>` with the public URL shown
by Render and open:

- `<your-render-service-url>/health`
- `<your-render-service-url>/docs`

The health endpoint should return `{"status":"ok"}` and `/docs` should display
the FastAPI Swagger UI. When a new commit is pushed to the connected GitHub
branch, Render automatically starts a new deployment. Build and runtime logs
are available on the service's **Logs** tab in the Render dashboard.