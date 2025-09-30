// Script pour mettre à jour tous les menus des pages de produits
// Ce script doit être utilisé manuellement pour modifier les fichiers

const fs = require('fs');
const path = require('path');

// Menu HTML moderne avec burger
const newMenuHtml = `    <header class="main-header">
        <div id="logo">
            <a href="../index.html">
                <img src="../images/assoc.png" alt="Logo de l'association">
            </a>
        </div>

        <!-- Menu burger pour mobile -->
        <button class="menu-burger" id="menu-burger" aria-label="Ouvrir le menu">
            <span></span>
            <span></span>
            <span></span>
        </button>

        <nav class="main-nav" data-test="menu-navigation" aria-label="Menu principal" id="main-nav">
            <ul>
                <li><a href="../index.html">Accueil</a></li>
                <li><a href="../quisommesnous.html">Qui sommes-nous ?</a></li>
                <li><a href="../index.html#produits-featured">Produits</a></li>
                <li><a href="../index.html#categories-section">Catégories</a></li>
                <li><a href="../index.html#contact">Contact</a></li>
                <li><a href="../faq.html">FAQ</a></li>
                <li><a href="../connexion.html">Profil</a></li>
                <li>
                    <a href="../panier.html" class="icone-panier" aria-label="Voir le panier">
                        <img src="../images/panier.png" alt="Panier" />
                        <span id="compteur-panier">0</span>
                    </a>
                </li>
            </ul>
        </nav>
    </header>`;

// JavaScript pour le menu burger
const burgerScript = `
        // Script pour le menu burger mobile
        const menuBurger = document.getElementById("menu-burger");
        const mainNav = document.getElementById("main-nav");
        
        if (menuBurger && mainNav) {
            menuBurger.addEventListener("click", () => {
                mainNav.classList.toggle("nav-open");
                menuBurger.classList.toggle("menu-open");
            });

            // Fermer le menu quand on clique sur un lien
            const navLinks = mainNav.querySelectorAll("a");
            navLinks.forEach(link => {
                link.addEventListener("click", () => {
                    mainNav.classList.remove("nav-open");
                    menuBurger.classList.remove("menu-open");
                });
            });

            // Fermer le menu quand on clique en dehors
            document.addEventListener("click", (e) => {
                if (!mainNav.contains(e.target) && !menuBurger.contains(e.target)) {
                    mainNav.classList.remove("nav-open");
                    menuBurger.classList.remove("menu-open");
                }
            });
        }`;

// Fichiers de produits à mettre à jour
const productFiles = [
    'produits_phares/benchou-ferrari.html',
    'produits_phares/casque-sony-wh1000xm4.html',
    'produits_phares/doudoune-ski.html',
    'produits_phares/maillot-fc-barcelone.html',
    'produits_phares/montre-fossil.html',
    'produits_phares/nike-air-force-1-07lvb.html',
    'produits_phares/parfum-azzaro-sport.html',
    'produits_phares/robe-ete-zara.html',
    'produits_phares/sac-longchamp.html',
    'produits_phares/sneakers-adidas-ultraboost.html',
    'produits_phares/sweatshirt-ovs-break-filles.html'
];

console.log('Fichiers de produits à mettre à jour:');
productFiles.forEach(file => console.log(`- ${file}`));