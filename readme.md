# api-htas-ai
Provides diferent tools made using Transformer Model. <br>
- Translate
- Extract Keyworks
- Paraphrase
- Summarize
- Analyse sentiment

## Docker
I recommend deploy your application as a Docker image.<br>

  `docker build -t api-ai-tools .`

Once your image has been built and loaded locally, run your application by running:<br>
 `docker run --env-file .env -p 5000:5000  api-ai-tools`

