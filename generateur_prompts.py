# Générateur de prompts pour ton entreprise
# Avec base de données de termes et phrases réutilisables

import random

# Base de données de termes et phrases réutilisables pour ton secteur
base_de_donnees = {
    "technologies": [
        "Intelligence Artificielle", "Blockchain", "Cloud Computing",
        "DevOps", "Cybersécurité", "Internet des Objets (IoT)",
        "Big Data", "SaaS", "PaaS", "Machine Learning"
    ],
    "publics_cibles": [
        "Développeurs", "CTO", "Startups", "Investisseurs",
        "Grand Public", "Étudiants en technologie"
    ],
    "tons": [
        "Technique", "Pédagogique", "Convaincant", "Inspirant",
        "Professionnel", "Simplifié", "Analytique"
    ],
    "appels_action": [
        "Essayez notre démo gratuite",
        "Contactez-nous pour une consultation",
        "Téléchargez notre livre blanc",
        "Inscrivez-vous à notre webinaire",
        "Découvrez nos études de cas"
    ]
}

def generer_prompt(
    type_contenu,
    public_cible,
    sujet,
    ton,
    elements_cles,
    longueur=None,
    style_artistique=None,
    elements_visuels=None,
    palette_couleurs=None,
    ambiance=None,
):
    """
    Génère un prompt personnalisé pour ton entreprise.
    """
    technologie_aleatoire = random.choice(base_de_donnees["technologies"])
    appel_action_aleatoire = random.choice(base_de_donnees["appels_action"])

    if type_contenu.lower() == "image":
        prompt = (
            f"Crée une image {style_artistique} représentant {sujet}. "
            f"Inclure {elements_visuels} et utiliser une palette de couleurs {palette_couleurs}. "
            f"Ambiance : {ambiance}. "
            f"Mettre en avant la technologie : {technologie_aleatoire}."
        )
    else:
        prompt = (
            f"Rédige un {type_contenu} pour {public_cible} sur le thème de {sujet}. "
            f"Le ton doit être {ton}. Inclure : {elements_cles}, "
            f"et un appel à l’action : '{appel_action_aleatoire}'. "
            f"Longueur : {longueur}."
        )
    return prompt

# Exemples d'utilisation
if __name__ == "__main__":
    exemple_article = generer_prompt(
        type_contenu="article technique",
        public_cible="développeurs",
        sujet="l'intégration de l'IA dans les applications SaaS",
        ton="pédagogique",
        elements_cles="exemples de code, bonnes pratiques, études de cas",
        longueur="1500 mots"
    )

    exemple_image = generer_prompt(
        type_contenu="image",
        sujet="une architecture cloud moderne",
        style_artistique="futuriste",
        elements_visuels="diagrammes d'architecture, icônes de services cloud",
        palette_couleurs="bleu électrique et noir",
        ambiance="moderne et professionnelle"
    )

    print("Exemple de prompt pour un article :\n", exemple_article, "\n")
    print("Exemple de prompt pour une image :\n", exemple_image)

