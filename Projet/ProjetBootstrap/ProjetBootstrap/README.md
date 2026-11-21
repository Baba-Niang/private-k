# Projet Bootstrap 5 - Site vitrine d'entreprise

Projet réalisé avec **HTML5**, **CSS3** et **Bootstrap 5** (chargé en ligne via CDN, comme conseillé
pour l'apprentissage — voir le guide https://baba-niang.github.io/Guide-Bootstrap-Bigginers/).

## Comment lancer le site
Il n'y a rien à installer. Ouvrez simplement `index.html` dans votre navigateur
(double-clic sur le fichier), ou utilisez l'extension "Live Server" de VS Code.

## Arborescence
```
ProjetBootstrap/
├── index.html      → Accueil (navbar, hero, présentation, aperçu services, statistiques, témoignages)
├── services.html   → 6 cartes de services + accordéon FAQ
├── galerie.html    → Galerie de 12 images (4 col desktop / 3 col tablette / 2 col mobile) + modale + pagination
├── equipe.html     → 4 membres de l'équipe
├── contact.html    → Formulaire de contact avec validation, spinner et alerte
├── css/
│   └── style.css   → Personnalisation (couleurs, polices Google Fonts, effets de survol, animations, ombres, coins arrondis)
└── js/
    └── script.js   → Interactions (lien de nav actif, envoi du formulaire, modale galerie)
```

## Composants Bootstrap utilisés (cahier des charges)
| Composant        | Où le trouver                                  |
|-------------------|-------------------------------------------------|
| Navbar responsive | Toutes les pages (fixe + bouton hamburger)      |
| Grid / Container / Row / Col | Toutes les pages                     |
| Cards             | Services, statistiques, témoignages, équipe     |
| Buttons           | Toutes les pages (dont `btn-outline-*`)         |
| Carousel          | Section témoignages (index.html)                |
| Accordion         | FAQ (services.html)                             |
| Modal             | Lightbox de la galerie (galerie.html)           |
| Alerts            | Confirmation d'envoi (contact.html)             |
| Badges            | Services "Populaire" / "Nouveau"                |
| Pagination        | Bas de la galerie (galerie.html)                |
| Breadcrumb        | Haut de chaque page secondaire                  |
| Collapse          | Bouton "En savoir plus" (index.html)            |
| Spinner           | Bouton "Envoyer" du formulaire (contact.html)   |
| Progress bar      | Section statistiques (index.html)               |
| Forms             | Formulaire de contact avec validation Bootstrap |
| Utilities         | Espacements, couleurs, ombres, arrondis partout |

## Remarque sur les images
Les images utilisent le service gratuit **picsum.photos** en attendant vos vraies photos
(logo, bannière, équipe, services, galerie). Il suffit de remplacer les `src="https://picsum.photos/..."`
par vos propres fichiers dans le dossier `images/` (ex : `images/equipe1.jpg`).

## Personnalisation
Toutes les couleurs, polices et animations sont centralisées dans `css/style.css`,
avec des variables CSS (`:root`) faciles à modifier en haut du fichier.
