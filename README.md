# mcp-server-google-vision

Serveur MCP [Model Context Protocol](https://modelcontextprotocol.io/introduction) permettant aux LLMs comme Claude de lire des documents scannés, du texte manuscrit et des images avec l'API Google Cloud Vision.

## Description

Ce projet implémente un serveur MCP qui donne des capacités de vision avancées aux modèles de langage. Développé par [Kohen Avocats](https://kohenavocats.com), un cabinet d'avocats parisien, cet outil est utilisé quotidiennement pour traiter des documents juridiques complexes : pièces scannées, courriers manuscrits, PDF mal orientés, etc.

### Le problème résolu

Les LLMs comme Claude excellent dans l'analyse de texte, mais ne peuvent pas nativement :
- Lire des PDF scannés (images sans couche texte)
- Déchiffrer l'écriture manuscrite
- Traiter des documents mal orientés ou inversés
- Extraire du texte de photos de documents

Ce serveur MCP comble cette lacune en fournissant une interface standardisée vers Google Cloud Vision, permettant aux LLMs de "voir" et lire n'importe quel document.

### Cas d'usage

- **Cabinets d'avocats** : Lecture de pièces scannées, correspondances manuscrites, documents anciens
- **Alimentation de RAG** : Extraction de texte pour indexation dans des bases vectorielles
- **Traitement documentaire** : OCR de masse avec gestion automatique des PDFs multi-pages
- **Accessibilité** : Transcription de documents pour personnes malvoyantes

### Fonctionnalités clés

- **OCR haute précision** : Reconnaissance de texte imprimé et manuscrit
- **Support multi-pages** : Traitement parallèle des PDFs jusqu'à 2000 pages
- **Détection d'orientation** : Lecture correcte même si le document est à l'envers
- **9 features Vision API** : text, document, labels, faces, objects, logos, landmarks, web, safe_search
- **Retry intelligent** : Backoff exponentiel avec jitter pour une fiabilité maximale
- **Unicode robuste** : Gestion des noms de fichiers avec accents et caractères spéciaux

## Prérequis

- Python 3.11+
- Une clé API Google Cloud Vision ([obtenir ici](https://console.cloud.google.com/apis/credentials))
- Un LLM compatible MCP (Claude Desktop, etc.)

## Installation

### 1. Créer et activer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

Ou avec uv :
```bash
uv venv .venv
source .venv/bin/activate
```

### 2. Installer le package

Via pip (depuis PyPI) :
```bash
pip install mcp-server-google-vision
```

Via uv :
```bash
uv pip install mcp-server-google-vision
```

Ou depuis GitHub :
```bash
pip install git+https://github.com/KohenAvocats/mcp-server-google-vision.git
```

### 3. Configurer la clé API

Créez un fichier `.env` :
```
GOOGLE_API_KEY=votre_clé_api_google
```

Ou exportez la variable :
```bash
export GOOGLE_API_KEY="votre_clé_api_google"
```

## Configuration avec Claude Desktop

La méthode la plus simple consiste à utiliser `uvx` (nécessite l'installation de [uv](https://astral.sh/uv/)) :

```json
{
  "mcpServers": {
    "google-vision": {
      "command": "uvx",
      "args": ["--from", "mcp-server-google-vision", "mcp-google-vision"],
      "env": {
        "GOOGLE_API_KEY": "votre_clé_api"
      }
    }
  }
}
```

Alternativement, si vous avez installé le package via pip :

```json
{
  "mcpServers": {
    "google-vision": {
      "command": "python",
      "args": ["-m", "mcp_server_google_vision"],
      "env": {
        "GOOGLE_API_KEY": "votre_clé_api"
      }
    }
  }
}
```

## Outils disponibles
... (reste de la section)

## Architecture technique

```
mcp-server-google-vision/
├── src/
│   └── mcp_server_google_vision/
│       ├── __init__.py
│       ├── __main__.py
│       └── server.py          # Serveur MCP principal
├── pyproject.toml             # Configuration du package
├── smithery.yaml              # Configuration Smithery
├── README.md                  # Documentation
└── LICENSE                    # Licence MIT
```

### Points techniques notables

- **Session HTTP réutilisable** : Pool de 20 connexions pour performances optimales
- **Retry avec backoff exponentiel** : Délai initial 1s, max 60s, multiplicateur 2x
- **Gestion Unicode** : Support des caractères spéciaux français (accents, apostrophes typographiques)
- **Traitement parallèle** : `asyncio.gather` pour les PDFs multi-pages

## Limitations

- Taille maximale des PDFs : 20 MB
- Requêtes limitées par les quotas Google Cloud Vision
- Connexion internet requise

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Ouvrir une issue pour signaler un bug
- Proposer une pull request pour une amélioration
- Partager vos cas d'usage

## Auteur

Développé par [Maître Hassan KOHEN, avocat pénaliste à Paris](https://kohenavocats.com/avocat-hassan-kohen/), fondateur de [Kohen Avocats](https://kohenavocats.com).

Ce serveur MCP est né d'un besoin concret : permettre à Claude d'analyser les pièces d'un dossier juridique, y compris les documents scannés et manuscrits. Il est aujourd'hui utilisé quotidiennement au cabinet pour :
- La lecture de pièces adverses scannées
- L'analyse de correspondances manuscrites
- L'alimentation d'un RAG juridique interne

## Liens utiles

- [Kohen Avocats - Cabinet d'avocats Paris](https://kohenavocats.com)
- [Maître Hassan KOHEN, avocat pénaliste à Paris](https://kohenavocats.com/avocat-hassan-kohen/)
- [Package PyPI](https://pypi.org/project/mcp-server-google-vision/)
- [Model Context Protocol](https://modelcontextprotocol.io/introduction)
- [Google Cloud Vision API](https://cloud.google.com/vision/docs)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Licence

[MIT License](LICENSE)

---

*Ce projet est open source et peut être librement utilisé, modifié et redistribué sous licence MIT.*
