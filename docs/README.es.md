# Resume Guide - Generador de Curriculum Interactivo

> **Claude Code Skill** — Un plugin de skill para [Claude Code](https://claude.ai/code)

**[English](../README.md)** | **[中文](README.zh-CN.md)** | **[日本語](README.ja.md)**

Un asistente profesional de curriculum que recopila tu información a través de una conversación amigable y paciente de múltiples turnos, y luego genera un curriculum PDF pulido.

## Características

- **Conversacional** — Interacción en lenguaje natural, sin formularios
- **5 Niveles de optimización** — Desde reproducción fiel hasta pulido máximo
- **Multilingüe** — Curriculum en chino / inglés
- **Múltiples plantillas** — Tech, Classic, Modern
- **Persistencia de datos** — Guarda y revisa curriculums en cualquier momento

## Plantillas disponibles

| Plantilla | Descripción |
|-----------|-------------|
| `tech_zh` | Tecnológico · Chino |
| `tech_en` | Tecnológico · Inglés |
| `classic_zh` | Clásico · Chino |
| `classic_en` | Clásico · Inglés |
| `modern_zh` | Moderno · Chino (diseño con barra lateral) |
| `modern_en` | Moderno · Inglés (diseño con barra lateral) |

## Requisitos previos

- [Claude Code](https://claude.ai/code) — Asistente oficial de programación IA de Anthropic
- Python 3.6+
- pip3

## Instalación

### Opción 1: Instalación con un clic (Recomendado)

Ejecuta este comando en Claude Code:

```
/install https://github.com/wsdone/resume-guide
```

### Opción 2: Script de instalación

```bash
git clone https://github.com/wsdone/resume-guide.git
cd resume-guide
chmod +x install.sh
./install.sh
```

O usa curl:

```bash
curl -fsSL https://raw.githubusercontent.com/wsdone/resume-guide/main/install.sh | bash
```

### Opción 3: Instalación manual

```bash
git clone https://github.com/wsdone/resume-guide.git
cp -r resume-guide ~/.claude/skills/
pip3 install -r ~/.claude/skills/resume-guide/scripts/requirements.txt
```

## Uso

Después de la instalación, escribe en **Claude Code**:

```
/resume-guide
```

El skill primero te pedirá que elijas un idioma y luego te guiará a través del proceso de creación del curriculum.

## Dependencias

- Python 3.6+
- weasyprint (HTML a PDF)
- Jinja2 (renderizado de plantillas)

## Licencia

MIT License

## Proyectos relacionados

- [interview-coach](https://github.com/wsdone/interview-coach) — Entrenador de entrevistas IA

## Contribuir

¡Se agradecen los Issues y Pull Requests!
