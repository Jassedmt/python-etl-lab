# 💰 Reto #2: Consolidación Financiera Multi-divisa

## 🧠 Contexto del negocio
El cliente **GlobalPay Solutions** procesa pagos internacionales en múltiples divisas.

Actualmente reciben transacciones en:
- Dólares (**USD**)
- Libras (**GBP**)
- Euros (**EUR**)

Sin embargo, su contabilidad central en España opera únicamente en **Euros (EUR)**.

👉 Necesitan un script que:
- Unifique todas las transacciones
- Convierta los montos a EUR
- Calcule el valor real de su cartera financiera

---

## 📝 Especificaciones Técnicas (Requerimientos)

### 🔹 1. Extracción
- Archivo de entrada: `03_Finanzas_Crypto/data/pagos_raw.txt`
- Separador: `,` (coma)

**Formato de cada fila:**
ID_Transaccion,Cliente,Monto,Divisa

---

### 🔹 2. Transformación (El núcleo del reto)

#### 💱 Tasas de Cambio
Utiliza un **diccionario en Python** para definir las conversiones:

- 1 USD = 0.92 EUR  
- 1 GBP = 1.17 EUR  

---

#### 🔄 Conversión de Divisas
- Si la divisa es **USD** o **GBP** → convertir a EUR usando su tasa correspondiente  
- Si la divisa es **EUR** → mantener el valor original  

---

#### 🔢 Redondeo
- El monto final en euros debe tener **2 decimales**
- Usa: `round(valor, 2)`

---

#### 🧹 Limpieza de Datos
- El campo **Cliente** puede contener espacios innecesarios  
- Elimina espacios al inicio y al final  

---

### 🔹 3. Carga (Output)
- Guardar el archivo en:  
  `03_Finanzas_Crypto/output/pagos_consolidados.csv`

**Columnas finales:**
- ID  
- Cliente  
- Monto_Original  
- Divisa_Original  
- Monto_EUR  

---

## 🧪 Datos de Entrada (data/pagos_raw.txt)

- TXN001, Alice Smith ,150.50,USD
- TXN002, Bob Jones ,85.00,GBP
- TXN003,Charlie Brown,200.00,EUR
- TXN004, Diana Prince ,1250.75,USD
- TXN005,Edward Norton,45.20,GBP

---

## 🎯 Objetivo
Construir un pipeline que:
- Limpie los datos de entrada  
- Convierta correctamente todas las divisas a EUR  
- Genere un dataset consolidado listo para análisis financiero  