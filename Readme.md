# Chatbot

## Before your start

This README would normally document whatever steps are necessary to get your application up and running.

![Python : 12](https://img.shields.io/badge/Python-=3.12-green)

### Vidéo d'utilisation

https://youtu.be/Bn6CVXCIfLs

### Lectures recommandées

* [Flask framework](https://flask.palletsprojects.com/en/1.1.x/)
* [flask-design-pattern](https://github.com/topics/flask-design-pattern)
* [Application Factories](https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/#basic-factories)
* [Structuring a Large Production Flask Application](https://levelup.gitconnected.com/structuring-a-large-production-flask-application-7a0066a65447)
* [Flask Design Patterns And Best Practices For Web Applications](https://www.softwaretestinghelp.com/flask-design-patterns-for-web-applications/)
* [Flask-RESTx](https://flask-restx.readthedocs.io/en/latest/index.html)
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)
* [Markdown support in content](https://daringfireball.net/projects/markdown/syntax)

### Coding standard

#### Branches Git

| Branche   | Usage                                                                                    |
|:----------|:-----------------------------------------------------------------------------------------|
| master    | Branche de production, livrée sur les environnements de production                       |
| develop   | Branche intégrant les features et les fix en cours de validation par l'équipe technique. |
|           |                                                                                          |
| feature/* | Branches dédiées au développement des fonctionnalités.                                   |
| bugfix/*  | Branches dédiées au traitement des corrections.                                          |
| hotfix/*  | Branches dédiées au traitements des hotfix.                                              |
|           |                                                                                          |

##### Création d'une branche de fonctionnalité

Partir d'une version à jour de develop

```bash
git checkout develop
git fetch origin
git reset --hard origin/develop
```

Créer la nouvelle branche, ici appelée *name*

```bash
git checkout -b feature/name
```

Pour le premier commit sur la branche

```bash
git status
git add [files]
git commit -m "commit message"
git push -u origin feature/name
```

Les commits suivants pourront se faire en utilisant git push directement, sans les paramètres supplémentaires.

Pour s'assurer que la branche est à jour vis-à-vis de develop avant de réaliser un merge dedans :

```bash
git pull origin develop
```

Pour réaliser le merge dans develop

```bash
git checkout develop
git pull origin feature/name
git push
```

#### Environnement de développement

* Éditeur de code : **VSCode**
* Extensions recommandées (Python)
  * Python
  * isort
* Extensions recommandées (Génériques)
  * GitLens
  * Better Comments
  * markdownlint
  * Markdown Preview Mermaid Support

### Installation locale

Initialiser l'environnement Python :

```shell
make init-project
```

Lancer le serveur Flask :

```shell
make run-local
```