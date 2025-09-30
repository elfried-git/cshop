#!/usr/bin/env python3
"""
Script pour moderniser automatiquement toutes les pages de produits restantes
"""

import os
import re

def replace_header_in_file(filepath):
    """Remplace l'ancien header par le header moderne dans un fichier"""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"Traitement de {os.path.basename(filepath)}...")
        
        # Pattern pour l'ancien header (plus flexible)
        old_header_pattern = r'<header class="main-header">.*?</header>'
        
        # Header moderne de remplacement
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
        
        # Remplacer l'ancien header
        new_content = re.sub(old_header_pattern, modern_header, content, flags=re.DOTALL)
        
        # Ajouter le JavaScript moderne s'il n'existe pas déjà
        js_pattern = r'document\.addEventListener\("DOMContentLoaded", \(\) => \{'
        
        if 'mobile-menu-toggle' not in content:
            # Chercher où insérer le JS moderne
            js_insertion_point = re.search(js_pattern, new_content)
            if js_insertion_point:
                insert_pos = js_insertion_point.end()
                
                modern_js = '''
            updateCartCounter();

            // Navigation moderne - Menu mobile
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
                
                # Insérer le JS moderne
                new_content = new_content[:insert_pos] + modern_js + new_content[insert_pos:]
        
        # Sauvegarder le fichier modifié
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ {os.path.basename(filepath)} modernisé avec succès!")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du traitement de {os.path.basename(filepath)}: {e}")
        return False

def main():
    """Fonction principale"""
    # Pages à traiter (exclure celles déjà traitées)
    pages_to_process = [
        "doudoune-ski.html",
        "sac-longchamp.html", 
        "montre-fossil.html",
        "maillot-fc-barcelone.html",
        "parfum-azzaro-sport.html",
        "robe-ete-zara.html",
        "sneakers-adidas-ultraboost.html",
        "nike-air-force-1-07lvb.html",
        "casque-sony-wh1000xm4.html"
    ]
    
    products_dir = "c:/Users/e.mongo/Desktop/proj/SiteEcommerce/produits_phares"
    
    success_count = 0
    for filename in pages_to_process:
        filepath = os.path.join(products_dir, filename)
        if os.path.exists(filepath):
            if replace_header_in_file(filepath):
                success_count += 1
        else:
            print(f"⚠️ Fichier non trouvé: {filename}")
    
    print(f"\n✨ Modernisation terminée!")
    print(f"📊 {success_count}/{len(pages_to_process)} pages modernisées avec succès")

if __name__ == "__main__":
    main()