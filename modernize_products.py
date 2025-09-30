#!/usr/bin/env python3
"""
Script pour moderniser automatiquement toutes les pages de produits
"""

import os
import re
import glob

def modernize_product_page(filepath):
    """Modernise une page de produit en remplaçant l'ancien header par le moderne"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"Traitement de {filepath}...")
        
        # 1. Mettre à jour le title et ajouter les CSS modernes
        title_pattern = r'(<title>)[^<]*(</title>)'
        css_pattern = r'(\s*<link rel="stylesheet" href="\.\./global\.css">)\s*(<link rel="stylesheet" href="\.\./detailproduit\.css">)'
        
        # Extraire le nom du produit depuis le nom de fichier
        filename = os.path.basename(filepath).replace('.html', '').replace('-', ' ').title()
        
        # Remplacer le title
        content = re.sub(title_pattern, rf'\1{filename} - Shop Na Biso\2', content)
        
        # Ajouter les CSS modernes
        modern_css = '''    <link rel="stylesheet" href="../global.css">
    <link rel="stylesheet" href="../index-modern.css">
    <link rel="stylesheet" href="../detailproduit.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">'''
        
        content = re.sub(css_pattern, modern_css, content)
        
        # 2. Remplacer l'ancien header par le moderne
        old_header_pattern = r'<header class="main-header">.*?</header>'
        
        modern_header = '''    <!-- Navigation moderne -->
    <header class="modern-header">
        <nav class="nav-container">
            <div class="nav-brand">
                <a href="../index.html" class="brand-link">
                    <div class="brand-icon">
                        <i class="fas fa-shopping-bag"></i>
                    </div>
                    <span class="brand-text">Shop Na Biso</span>
                </a>
            </div>

            <div class="nav-menu" id="nav-menu">
                <ul class="nav-list">
                    <li><a href="../index.html" class="nav-link">Accueil</a></li>
                    <li><a href="../quisommesnous.html" class="nav-link">À propos</a></li>
                    <li><a href="../index.html#produits-featured" class="nav-link">Produits</a></li>
                    <li><a href="../index.html#categories-section" class="nav-link">Catégories</a></li>
                    <li><a href="../index.html#contact" class="nav-link">Contact</a></li>
                </ul>
            </div>

            <div class="nav-actions">
                <div class="currency-selector">
                    <select id="country-selector" class="currency-select">
                        <option value="EUR">EUR (€)</option>
                        <option value="XAF">FCFA</option>
                        <option value="USD">USD ($)</option>
                    </select>
                </div>
                <a href="../connexion.html" class="action-btn login-btn">
                    <i class="fas fa-user"></i>
                </a>
                <a href="../panier.html" class="action-btn cart-btn">
                    <i class="fas fa-shopping-cart"></i>
                    <span class="cart-count" id="compteur-panier">0</span>
                </a>
                <button class="mobile-menu-toggle" id="mobile-menu-toggle">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
        </nav>
    </header>'''
        
        content = re.sub(old_header_pattern, modern_header, content, flags=re.DOTALL)
        
        # 3. Ajouter le JavaScript moderne pour le menu mobile
        js_pattern = r'(document\.addEventListener\("DOMContentLoaded", \(\) => \{\s*updateCartCounter\(\);)'
        
        modern_js_addition = '''            // Navigation moderne - Menu mobile
            const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
            const navMenu = document.getElementById('nav-menu');
            
            if (mobileMenuToggle && navMenu) {
                mobileMenuToggle.addEventListener('click', () => {
                    navMenu.classList.toggle('nav-open');
                    mobileMenuToggle.classList.toggle('menu-open');
                });

                // Fermer le menu mobile quand on clique sur un lien
                const navLinks = navMenu.querySelectorAll('.nav-link');
                navLinks.forEach(link => {
                    link.addEventListener('click', () => {
                        navMenu.classList.remove('nav-open');
                        mobileMenuToggle.classList.remove('menu-open');
                    });
                });

                // Fermer le menu quand on clique en dehors
                document.addEventListener('click', (e) => {
                    if (!navMenu.contains(e.target) && !mobileMenuToggle.contains(e.target)) {
                        navMenu.classList.remove('nav-open');
                        mobileMenuToggle.classList.remove('menu-open');
                    }
                });
            }

'''
        
        content = re.sub(js_pattern, rf'\1\n\n{modern_js_addition}', content)
        
        # Sauvegarder le fichier modifié
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {filepath} modernisé avec succès!")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du traitement de {filepath}: {e}")
        return False

def main():
    """Fonction principale"""
    # Répertoire des produits phares
    products_dir = "c:/Users/e.mongo/Desktop/proj/SiteEcommerce/produits_phares"
    
    # Trouver tous les fichiers HTML (sauf ceux déjà traités)
    html_files = glob.glob(os.path.join(products_dir, "*.html"))
    
    # Exclure les fichiers déjà traités
    already_processed = [
        "sweatshirt-ovs-break-filles.html",
        "iphone-14-pro-max.html", 
        "nike-air-force-1-07lvb.html"
    ]
    
    files_to_process = []
    for filepath in html_files:
        filename = os.path.basename(filepath)
        if filename not in already_processed:
            files_to_process.append(filepath)
    
    print(f"🚀 Modernisation de {len(files_to_process)} pages de produits...")
    
    success_count = 0
    for filepath in files_to_process:
        if modernize_product_page(filepath):
            success_count += 1
    
    print(f"\n✨ Modernisation terminée!")
    print(f"📊 {success_count}/{len(files_to_process)} pages modernisées avec succès")

if __name__ == "__main__":
    main()