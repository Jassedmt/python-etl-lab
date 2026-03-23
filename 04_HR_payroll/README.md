# 👔 Reto #3: Nóminas y Gestión de IRPF (Recursos Humanos)

## 🧠 Contexto del negocio
El cliente **TechSolutions HR** tiene un problema con su sistema antiguo de nóminas.

👉 El sistema exporta archivos donde:
- A veces faltan datos
- El formato del salario es inconsistente

Necesitan calcular el **salario neto mensual** de los empleados aplicando un impuesto (**IRPF**).

---

## 📝 Especificaciones Técnicas (Requerimientos)

### 🔹 1. Extracción
- Archivo de entrada: `04_HR_Payroll/data/empleados_raw.txt`
- Separador: `;`

**Formato de cada fila:**
ID;Nombre;Departamento;Salario_Bruto_Anual

---

### 🔹 2. Transformación (El reto de hoy)

#### 💰 Limpieza de Salario
- El salario viene como texto (ej: `"30000"`)
- Debes convertirlo a `float`

---

#### ⚠️ Manejo de Errores (Clave del reto)
- Si el salario está vacío o no es un número:
  - NO debe romperse el programa
  - Asignar salario = `0.0`
  - Modificar el nombre a: `REVISAR: [Nombre]`

---

#### 🧮 Cálculo del Neto Mensual
- **IRPF**: aplicar una retención fija del 19%  
  → equivalente a multiplicar por `0.81`

- **Mensualidad**: dividir entre 12 pagas  

**Fórmula:**
Neto_Mensual = (Bruto * 0.81) / 12

---

#### 🔢 Redondeo
- El resultado final debe tener **2 decimales**
- Usa: `round(valor, 2)`

---

### 🔹 3. Carga (Output)
- Guardar el archivo en:  
  `04_HR_Payroll/output/nominas_finales.csv`

**Columnas finales:**
- ID  
- Empleado  
- Departamento  
- Salario_Bruto  
- Neto_Mensual  

---

## 🧪 Datos de Entrada (data/empleados_raw.txt)
- E001;Maria Garcia;IT;35000
- E002;Jose Perez;Ventas;28000
- E003;Ana Lopez;IT;
- E004;Luis Rodriguez;RRHH;ERROR
- E005;Elena Sanz;Marketing;42000


---

## 🛠️ Consejos de tu superior

#### 🧩 Estructura de Control
Para evitar que el programa falle con datos incorrectos, usa `try...except`.

- En el `try`: intenta convertir el salario con `float()`
- En el `except (ValueError)`:  
  - Asigna salario = `0.0`  
  - Modifica el nombre a `REVISAR: [Nombre]`

---

#### 🔁 Modularidad
- Reutiliza tus funciones de **extracción** y **carga**
- Crea una nueva función de **transformación** adaptada a este reto

---

## 🎯 Objetivo
Construir un pipeline robusto que:
- Limpie datos inconsistentes  
- Maneje errores sin romper el flujo  
- Calcule correctamente el salario neto mensual  
- Genere un archivo listo para el equipo de RRHH  