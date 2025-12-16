# 💱 DólarBot - ETL Automatizado de Tipo de Cambio

Sistema ETL (Extract, Transform, Load) automatizado que monitorea el tipo de cambio del dólar en Perú, identifica oportunidades de arbitraje y envía reportes diarios por correo electrónico.

## 🎯 Características Principales

- **Extracción automatizada** de datos desde múltiples fuentes:
  - API oficial de SUNAT
  - Web scraping de 15+ casas de cambio peruanas
- **Análisis inteligente** de tasas de cambio:
  - Identificación de top 3 mejores tasas de compra/venta
  - Detección automática de oportunidades de arbitraje
  - Cálculo de variaciones porcentuales diarias
- **Notificaciones HTML** personalizadas vía Gmail con:
  - Reporte visual de mejores tasas
  - Comparativa con tipo de cambio oficial SUNAT
  - Alertas de oportunidades de arbitraje
- **Persistencia de datos** en Supabase (PostgreSQL)
- **Ejecución automática** mediante GitHub Actions (cron diario)

## 🏗️ Arquitectura

```
┌─────────────────┐
│  GitHub Actions │  ← Scheduler (Cron: 18:00 UTC)
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│           ETL Pipeline                   │
│  ┌──────────┐  ┌──────────┐  ┌────────┐│
│  │ Extract  │→ │Transform │→ │  Load  ││
│  └──────────┘  └──────────┘  └────────┘│
└─────────────────────────────────────────┘
         │                    │
         ▼                    ▼
┌─────────────────┐   ┌──────────────┐
│  Gmail Service  │   │   Supabase   │
│  (Notificación) │   │  (PostgreSQL)│
└─────────────────┘   └──────────────┘
```

## 🛠️ Stack Tecnológico

### Backend & API
- **FastAPI** - Framework web moderno y de alto rendimiento
- **SQLAlchemy** - ORM para gestión de base de datos
- **Pydantic** - Validación de datos y configuración

### Web Scraping
- **BeautifulSoup4** - Parsing HTML
- **Selenium** - Automatización de navegador para sitios dinámicos
- **Requests** - Cliente HTTP

### Infraestructura
- **Supabase** - Base de datos PostgreSQL en la nube
- **GitHub Actions** - CI/CD y automatización de tareas
- **Docker & Docker Compose** - Containerización
- **Redis** - Cache y message broker
- **Celery** - Task queue para procesamiento asíncrono

## 📦 Estructura del Proyecto

```
dolar/
├── app/
│   ├── api/              # Endpoints REST
│   ├── scraper/          # Módulos de extracción de datos
│   │   ├── get_sunat_dolar.py
│   │   └── top_3_cambio.py
│   ├── services/         # Lógica de negocio
│   │   ├── domain/       # Servicios de dominio
│   │   └── infrastructure/  # Servicios de infraestructura
│   │       └── gmail/    # Servicio de notificaciones
│   ├── db/               # Modelos y configuración de BD
│   └── core/             # Configuración central
├── .github/
│   └── workflows/
│       └── daily.yml     # GitHub Action para ejecución diaria
├── docker-compose.yml    # Orquestación de servicios
└── requirements.txt
```

## 🚀 Instalación y Uso

### Requisitos Previos
- Python 3.11+
- Docker & Docker Compose (opcional)
- Cuenta de Supabase
- Credenciales de Gmail con App Password

### Variables de Entorno

Crear archivo `.env` con:

```env
# SUNAT API
TOKEN_SUNAT_API=your_token

# Gmail
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
EMAIL_TO=recipient@gmail.com

# Supabase
SUPABASE_URL=your_supabase_url
SUPABASE_API_KEY=your_api_key
SUPABASE_PASSWORD=your_password
```

### Ejecución Local

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar ETL manualmente
python -m app.services.infrastructure.test_gmail

# Iniciar API
uvicorn app.main:app --reload
```

### Ejecución con Docker

```bash
# Levantar todos los servicios
docker-compose up -d

# Ver logs
docker-compose logs -f app
```

## 📊 Funcionalidades del ETL

### 1. Extracción (Extract)
- Consulta API oficial de SUNAT para tipo de cambio del día
- Scraping de casas de cambio desde cuantoestaeldolar.pe
- Validación y limpieza de datos extraídos

### 2. Transformación (Transform)
- Cálculo de variaciones porcentuales vs día anterior
- Identificación de top 3 mejores tasas de compra/venta
- Detección de oportunidades de arbitraje
- Generación de badges visuales (▲/▼) para variaciones

### 3. Carga (Load)
- Inserción en Supabase con validación de duplicados
- Generación de reporte HTML personalizado
- Envío de notificación por Gmail

## 🤖 Automatización con GitHub Actions

El workflow se ejecuta automáticamente todos los días a las 13:00 (hora de Lima):

```yaml
on:
  schedule:
    - cron: '0 18 * * *'  # 18:00 UTC = 13:00 Lima
  workflow_dispatch:       # Ejecución manual
```

## 📧 Ejemplo de Reporte

El sistema genera reportes HTML con:
- 📈 Tipo de cambio oficial SUNAT con variación diaria
- 🏆 Top 3 mejores casas para comprar dólares
- 💰 Top 3 mejores casas para vender dólares
- ⚡ Alerta de oportunidades de arbitraje
- 🔗 Enlaces directos a cada casa de cambio

## 🔄 API Endpoints

```
GET  /                    # Info de la API
GET  /api/health          # Health check
GET  /api/v1/dolar        # Obtener datos de dólar
POST /api/v1/dolar        # Crear registro
```

## 📈 Mejoras Futuras

- [ ] Integración con WhatsApp Business API
- [ ] Dashboard web con gráficos históricos
- [ ] Alertas personalizadas por umbral de precio
- [ ] Soporte para más monedas (EUR, BRL, etc.)
- [ ] Machine Learning para predicción de tendencias

## 👨‍💻 Autor

**Jefersson** - [GitHub](https://github.com/tu-usuario)

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

⭐ Si este proyecto te resulta útil, considera darle una estrella en GitHub
