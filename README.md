# MedAuth AI — Agente de Pre-Autorización Quirúrgica

Sistema de auditoría médica con arquitectura RAG que reduce 
el tiempo de pre-autorización quirúrgica de días a segundos.

## Origen del proyecto

Este proyecto nació como respuesta a un reto inicial de hackIAthon. 
Ante el desafío de automatizar procesos médicos con IA, 
decidimos enfocarnos en uno de los cuellos de botella más 
críticos del sistema de salud: la pre-autorización quirúrgica. 
Lo que antes tomaba horas o días, ahora sucede en segundos.

## Demo en vivo

[Abrir MedAuth AI](https://dbolanos-s.github.io/medauth-IA)

## Tecnologías utilizadas

- Dify — Orquestación del agente IA
- Notion — Base de datos de pólizas e informes médicos
- RAG — Validación contra Manual de Coberturas CIE-10
- FastAPI — Proxy backend seguro
- Render — Despliegue del proxy
- GitHub Pages — Interfaz pública

## Arquitectura
Usuario → GitHub Pages (HTML) → Render (Proxy) → Dify (Agente) → Notion

## Bases de datos en Notion

### DB_Informes_Medicos
<img width="1656" height="241" alt="image" src="https://github.com/user-attachments/assets/09948c92-2f74-4a46-9272-ab188f6f9bcb" />

### DB_Polizas_Activas
<img width="1688" height="376" alt="image" src="https://github.com/user-attachments/assets/6d596b6b-324b-4ed1-9cd7-e5897a997f00" />

## Agente en Dify
<img width="1918" height="1045" alt="image" src="https://github.com/user-attachments/assets/c6deccac-db67-49bc-9c43-ba3f5873a4ae" />

## App funcionando
<img width="1895" height="1079" alt="App" src="https://github.com/user-attachments/assets/4a90e477-fa58-4199-9323-b26234331b2b" />

## Flujo de trabajo

1. Recibe informe médico con código CIE-10
2. Consulta póliza del paciente en Notion
3. Valida contra Manual de Coberturas RAG
4. Emite certificado de aprobación o solicitud de documentos

## Desarrollado por

- Domenica Bolaños
- Rafael Bolaños
