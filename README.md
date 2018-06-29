# Django y Celery en contenedores de Docker, para dev y producción
## 2018-06-28

Crear y consumir web APIs es fundamental para desarrollo web y mobile. Existen varios clientes HTTP que ayudan con esto. A grandes rasgos se dividen entre clientes GUI como Postman, Insomnia y Paw, y clientes CLI como cURL y HTTPie.

Requester es un cliente HTTP para Sublime Text. Combina elementos de managed UI propios de clientes GUI como colecciones, historial de peticiones, env vars y pruebas automatizadas, con la ligereza y rápidez de clientes CLI. Todo se trabaja con texto, lo cual hace trivial compartir y versionar colecciones de peticiones. Su sintaxis es poderoso y [muy bien documentado](http://docs.python-requests.org/en/master/).


## Preparación
### Para OSX
- Instalar [Docker](https://store.docker.com/editions/community/docker-ce-desktop-mac)
- Instalar Python 3.6 (`brew install python3`)

## Helpers
~~~sh
alias dkp='docker ps'
alias dk='docker-compose'

dkash () {
  docker exec -it $1 /bin/ash
}

dksh () {
  docker exec -it $1 /bin/bash
}
~~~


## Resumen
- Features básicos y sintaxis
  + Request Body, Query Params, Custom Headers, Cookies
  + Variables de ambiente
  + Sintaxis (Requests), Parser, y convenience methods
- UI y UX
  + Colecciones de peticiones y navegación
  + Pestañas de respuesta
  + Historial de peticiones
- Pruebas
  + Test Runner
    + Sintaxis
    + JSON Schema
    + Integración con build process (generar scripts de pruebas)
  + Métricas (Benchmarking Tool)
- Portabilidad y Equipos
  + Exportar a cURL, HTTPie
  + Importar de cURL
    * Debugging peticiones AJAX/XHR mandados por tu browser
    * <https://www.nytimes.com/>, `commentData.json`, `commentCount`
- Autenticación: Twitter API
  + Extensiones a Requester, `requests-oauthlib`
  + <https://developer.twitter.com/en/docs/api-reference-index>
  + Explorando hyperlinked APIs (HATEOAS)
- Bonus: GraphQL support
  + Guardando peticiones a su requester file


## Preguntas
