# LLM_API
Deze map bevat de python scripts, de Containerfile en het AI model om antwoorden mee te genereren. In de *model* map moet zelf een `.GGUF` bestand geladen worden. De API heeft een link voor het genereren van een antwoord. Dit geeft een `JSON` object terug wat een antwoord met en zonder context heeft gegenereerd, hier is voor gekozen om zo beter aan te kunnen tonen wat de verschillen/voordelen zijn.

De LLM_API wordt lokaal in een container gehost omdat het Openshift cluster niet voldoende resources heeft.

## Endpoint
- **/generate/** genereer