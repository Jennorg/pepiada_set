# Herramienta de Análisis de Demanda y Optimización de Inventario

Herramienta de análisis de datos para pequeños comercios (restaurantes, panaderías, cafeterías, talleres o microempresas manufactureras) orientada a predecir la demanda futura y calcular la cantidad óptima de materia prima a adquirir, reduciendo tanto el desabastecimiento como el desperdicio por sobrecompra.

## Estructura del Proyecto

```text
pepiada_set/
├── config/                  # Configuraciones globales (parámetros de inventario, rutas, .env)
├── data/
│   ├── raw/                 # Datos crudos originales (ventas, compras, almacén, recetas/BOM)
│   ├── processed/           # Datos limpios, estandarizados y estructurados
│   └── outputs/             # Resultados generados (proyecciones, alertas, órdenes sugeridas)
├── notebooks/               # Notebooks para exploración (EDA), tendencias y estacionalidad
├── reports/                 # Reportes automatizados generados por ciclo de compra
├── src/
│   ├── limpieza_datos/      # Limpieza, estandarización y validación de registros históricos
│   ├── recetas_merma/       # Explosión de materiales (recetas) y tasa de merma
│   ├── pronosticos/         # Modelos de pronóstico de demanda (promedios, suavizamiento, regresión)
│   ├── inventario_alertas/  # Punto de reorden, stock de seguridad, lead time y caducidad
│   ├── generador_reportes/  # Generación de reportes y cantidades sugeridas de compra
│   └── utilidades/          # Utilidades compartidas (conversión de unidades, I/O, helpers)
├── tests/                   # Pruebas unitarias y de validación de cálculos
├── codigo.py                # Script prototipo inicial de exploración CSV
├── prototipo.csv            # Dataset prototipo inicial
└── requirements.txt         # Dependencias del entorno Python
```

## Mapeo de Actividades

1. **Limpieza y estandarización (`src/limpieza_datos/`):** Normalización de fechas, unidades de medida (kg, litros, unidades), catálogos de productos/insumos y movimientos de almacén desde `data/raw/` hacia `data/processed/`.
2. **Explosión de materiales y merma (`src/recetas_merma/`):** Vinculación de ventas de productos terminados con el consumo proporcional de materias primas mediante recetas (BOM) ajustado por la tasa histórica de merma/desperdicio.
3. **Análisis y pronóstico de demanda (`notebooks/`, `src/pronosticos/`):** Estudio de tendencias y estacionalidad; aplicación de promedios móviles, suavizamiento exponencial o regresión para estimar consumo futuro.
4. **Control de inventario y alertas (`src/inventario_alertas/`):** Cálculo de stock de seguridad y punto de reorden según *lead time* de proveedores, existencias actuales y alertas de insumos críticos o próximos a vencer.
5. **Reportes automatizados (`src/generador_reportes/`, `reports/`):** Generación de reportes con las cantidades exactas de materia prima sugeridas para cada ciclo de compra.
