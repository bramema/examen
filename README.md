# 🧾 Sistema de Facturación para Restaurante

## 📌 Descripción

Este proyecto consiste en un **sistema de gestión y facturación para un restaurante**, desarrollado en **Python**.

El sistema funciona mediante un menú interactivo en consola y permite administrar diferentes elementos del restaurante, como:

* 📦 Productos
* 🪑 Mesas
* 👤 Clientes
* 🧾 Facturación
* 💰 Facturación con descuento

La información se almacena utilizando archivos **CSV** y **JSON**, permitiendo conservar los datos aunque el programa se cierre.

---

## 🚀 Funcionalidades

### 1. 📦 Gestión de productos

El sistema permite:

* Agregar nuevos productos.
* Registrar código del producto.
* Registrar nombre.
* Registrar valor.
* Registrar porcentaje de IVA.
* Consultar la lista de productos registrados.

Los productos se almacenan en:

```text
productos.csv
```

Ejemplo de producto:

```text
codigo,nombre,valor,IVA
001,Hamburguesa,20000,19
002,Pizza,30000,19
```

---

### 2. 🪑 Gestión de mesas

Permite registrar y consultar las mesas disponibles en el restaurante.

Cada mesa contiene:

* Código.
* Nombre.
* Puesto.

Los datos se almacenan en:

```text
mesas.csv
```

Ejemplo:

```text
codigo,nombre,puesto
1,Mesa 1,4
2,Mesa 2,6
```

---

### 3. 👤 Gestión de clientes

El sistema permite registrar clientes con la siguiente información:

* Identificación.
* Nombre.
* Teléfono.
* Correo electrónico.

Los clientes se almacenan en:

```text
clientes.csv
```

Ejemplo:

```text
identificación,nombre,teléfono,email
123456789,Juan Pérez,3001234567,juan@gmail.com
```

---

### 4. 🧾 Facturación

La opción de facturación permite seleccionar productos registrados mediante su código.

Para cada producto se solicita:

* Código.
* Cantidad.

El sistema calcula automáticamente:

```text
Subtotal = valor × cantidad
IVA = subtotal × (IVA / 100)
Total producto = subtotal + IVA
```

Finalmente se muestra el total de la factura.

Ejemplo:

```text
======= FACTURA =======

{'nombre': 'Hamburguesa',
 'cantidad': 2,
 'subtotal': 40000,
 'iva': 7600,
 'total': 47600}

TOTAL A PAGAR: 47600
```

---

### 5. 💰 Facturación con descuento

Esta opción permite generar una factura aplicando un descuento.

El usuario debe ingresar:

* Código de la mesa.
* Nombre del cliente.
* Total de la cuenta.
* Si desea aplicar descuento.
* Porcentaje de descuento.

El descuento permitido está entre **0% y 50%**.

La fórmula utilizada es:

```text
Valor descuento = total × (descuento / 100)

Total final = total - valor descuento
```

Por ejemplo:

```text
Total sin descuento: $100000
Descuento: 10%
Valor descuento: $10000
Total con descuento: $90000
```

La información de la factura se prepara para ser almacenada en formato JSON.

---

## 🗂️ Estructura del proyecto

Una estructura recomendada para el proyecto es:

```text
proyecto_restaurante/
│
├── main.py
├── productos.csv
├── mesas.csv
├── clientes.csv
└── facturas.json
```

### Archivos

| Archivo         | Descripción                         |
| --------------- | ----------------------------------- |
| `main.py`       | Contiene el programa principal      |
| `productos.csv` | Almacena los productos              |
| `mesas.csv`     | Almacena las mesas                  |
| `clientes.csv`  | Almacena los clientes               |
| `facturas.json` | Almacena las facturas con descuento |

---

## 🛠️ Tecnologías utilizadas

El proyecto está desarrollado utilizando:

* **Python 3**
* `csv` — Para trabajar con archivos CSV.
* `json` — Para almacenar información en formato JSON.
* `pathlib` — Para manejar las rutas de los archivos.
* `match/case` — Para controlar las opciones del menú.

No se requieren librerías externas.

---

## ⚙️ Requisitos

Para ejecutar el proyecto necesitas:

* Python **3.10 o superior**, debido al uso de `match/case`.
* Un editor de código como:

  * Visual Studio Code
  * PyCharm
  * IDLE
* Sistema operativo Windows, Linux o macOS.

---

## ▶️ Instalación y ejecución

### 1. Clonar o descargar el proyecto

Descarga el proyecto en tu computador.

### 2. Abrir la carpeta

Abre la carpeta del proyecto desde tu editor de código.

### 3. Ejecutar el programa

Desde la terminal ejecuta:

```bash
python main.py
```

En algunos sistemas puede ser necesario utilizar:

```bash
python3 main.py
```

---

## 🖥️ Menú principal

Al iniciar el programa se mostrará:

```text
===========================================
=========== BIENVENIDO AL MENU ============
===========================================
1. productos
2. mesas
3. cliente
4. Facturacion
5. facturar con descuento
6. salir del menu
===========================================
```

El usuario puede seleccionar la opción que desea ejecutar.

---

## 💾 Manejo de archivos

El proyecto utiliza la función:

```python
guardar_csv()
```

para guardar información en archivos CSV.

También utiliza:

```python
cargar_csv()
```

para cargar los datos existentes cuando se inicia el programa.

Para las facturas se utiliza el módulo:

```python
json
```

permitiendo guardar información estructurada.

---

## 🔄 Flujo general del sistema

```text
              ┌─────────────────┐
              │     INICIO      │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  MENÚ PRINCIPAL │
              └────────┬────────┘
                       │
       ┌───────────────┼────────────────┐
       │               │                │
       ▼               ▼                ▼
  Productos          Mesas           Clientes
       │               │                │
       └───────────────┼────────────────┘
                       │
                       ▼
                ┌─────────────┐
                │ Facturación │
                └──────┬──────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Aplicar descuento│
              └────────┬─────────┘
                       │
                       ▼
                ┌─────────────┐
                │    Factura  │
                └─────────────┘



