


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 

# Créer les boutons de menu

st.sidebar.markdown("<span style='color:#F63366'>Menu</span>", unsafe_allow_html=True)

accueil_button = st.sidebar.button("Accueil")
description_button = st.sidebar.button("Description de la Dataframe")
analyse_button = st.sidebar.button("Analyse Préliminaire")
anastat_button = st.sidebar.button("Analyse Statistique")
barr_button = st.sidebar.button(" Mode de Consommation")

# Afficher le contenu en fonction du bouton cliqué
if accueil_button:
    st.title('Ethic Fashion')
    st.markdown('<span style="color: #87CEEB;">De la fast fashion à la mode éthique</span>', unsafe_allow_html=True)
    st.subheader("Auteurs: Christ BOUNDY, Aunice AHOUDJI, Nabil ABDENOURI, Sidik SANOGO ")
    st.write("Ce web service consiste à présenter les résultats de notre étude.")
    st.markdown('<h3 style="color: #87CEEB;">Introduction</h3>', unsafe_allow_html=True)
    st.write("La mode éthique est une réponse à l'impact négatif de l'industrie de la mode sur l'environnement et la société. Elle vise à adopter des pratiques responsables en matière de production, de distribution et de conditions de travail. Bien qu'elle soit en demande croissante, la mode éthique reste un marché de niche en raison de ses prix plus élevés et de sa disponibilité limitée.")
    st.write("L'industrie de la mode est l'une des industries les plus polluantes et les moins éthiques au monde, avec des conséquences dévastatrices sur l'environnement et les droits des travailleurs. Pour faire face à ces enjeux, de plus en plus de marques de mode se tournent vers une mode plus responsable, respectueuse de l'environnement et des droits des travailleurs. Cependant, la transition vers une industrie de la mode plus responsable est encore loin d'être achevée.")
    st.markdown('<h3 style="color: #87CEEB;">La Problèmatique</h3>', unsafe_allow_html=True)
    st.write("Comment pouvons-nous encourager cette transition vers une mode plus responsable ? ")
    st.write("Cette problématique est cruciale pour l'avenir de l'industrie de la mode et de notre planète, et nécessite des solutions innovantes et collectives.")
    st.markdown('<h3 style="color: #87CEEB;">L’objectif du projet</h3>', unsafe_allow_html=True)
    st.write("Avec l’aide de l’intelligence artificielle, nous allons développer un modèle d’apprentissage qui nous permettra de développer des solutions innovantes pour faciliter l'adoption de pratiques de consommation plus durables et éthiques.Nous allons procéder à l'analyse de données afin d'identifier les tendances, comportements et modes de consommation, ce qui nous permettra de prédire avec précision les consommateurs les plus susceptibles d'acheter des produits de mode éthique. Cette prédiction sera basée sur des facteurs tels que les informations démographiques, les attitudes et les comportements des consommateurs. Avec ces informations, nous serons en mesure de développer des solutions innovantes pour encourager l'adoption de pratiques de consommation plus durables et éthiques.")
    st.markdown('<h3 style="color: #87CEEB;">Démarche</h3>', unsafe_allow_html=True)
    st.write("- Collecte")
    st.write("- Analyse")
    st.write("- Modélisation")
    st.write("- Gestion de projet")
    
   
if description_button:

    st.title('Description de la DataFrame')
    st.markdown("<span style='color: #87CEEB;'>PRESENTATION DE LA DATAFRAME APRES L'ETAPE DU SCRAPING ET DU PRE-TRAITEMENT</span>", unsafe_allow_html=True)
    data= pd.read_csv("Finaldataset.csv")
    st.write(data.head())
    st.markdown("Cette dataframe est composée de 2799 lignes et de 19 colonnes avec des données de type 'object'.")
    st.markdown("Suite au nettoyage de la base de données, nous avons obtenu 2176 lignes valides représentant 77.2% de la base de données initiale et 19 colonnes. La description de chaque colonne ci dessous: ")
    st.markdown("<span style='color: #87CEEB;'>DESCRIPTION DE LA BASE DE DONNEE APRES L'ETAPE DE NETOYAGE DES DONNEE ET L'ENCODING</span>", unsafe_allow_html=True)
    
    from PIL import Image
    image = Image.open('des1.png')
    st.image(image, '')
    image = Image.open('des2.png')
    st.image(image, '')
    
    st.markdown('<span style="color: #87CEEB;">Informed consent</span>', unsafe_allow_html=True)
    st.write("La colonne 'Informed consent' indique que sur l'ensemble des réponses, 99,47% des participants ont donné leur consentement éclairé pour participer à l'étude, tandis que 0,53% n'ont pas donné leur consentement. Ces résultats montrent une forte adhésion des participants aux principes éthiques de la recherche, ce qui renforce la fiabilité et la validité des données collectées. Afin de fiabiliser nos résultats, nous avons enlevé tous les répondants ayant répondu “non” à cette question. ")
    st.markdown('<span style="color: #87CEEB;">Age</span>', unsafe_allow_html=True)
    st.write("La colonne 'Age' révèle que la majorité des participants (65,41%) sont âgés de 22 à 39 ans, suivis par les moins de 22 ans (25,97%). Les tranches d'âge intermédiaire sont moins représentées, avec seulement 5,60% des participants âgés de 39 à 52 ans et 2,87% âgés de 52 à 70 ans. Seuls 0,15% des participants sont âgés de 70 ans ou plus.")
    st.markdown('<span style="color: #87CEEB;">Gender</span>', unsafe_allow_html=True)
    st.write("La colonne 'Gender'' indique que sur l'ensemble des participants, 87,71% se sont identifiés comme étant de sexe féminin, tandis que 11,17% se sont identifiés comme étant de sexe masculin. Seuls 0,69% des participants ont déclaré appartenir à une autre catégorie de genre, et 0,44% ont préféré ne pas répondre. Ces résultats soulignent une forte représentation des femmes dans l'échantillon de participants, cependant tous les genres sont représentés.")
    
    st.markdown('<span style="color: #87CEEB;">Continent of residence</span>', unsafe_allow_html=True)
    st.write("La colonne 'Continent of residence' montre que la majorité des participants à l'étude résident en Amérique du Nord (64,91%), suivis de l'Europe (23,72%), de l'Asie (5,67%), de l'Australie (3,49%), de l'Amérique du Sud (1,63%), de l'Afrique (0,54%) et de l'Antarctique (0,04%). Ces résultats indiquent une représentation diversifiée de tous les  continents, bien que l'Afrique et l'Antarctique soient moins représentés.")
    
    st.markdown('<span style="color: #87CEEB;">Concerned about wasting resources</span>', unsafe_allow_html=True)
    st.write("Cette colonne 'Concerned about wasting resources' exprime une préoccupation ou une inquiétude que le répondant  peut avoir au sujet du gaspillage potentiel des ressources. Cela mesure si il valorise l’utilisation responsable des ressources et peut être motivée à prendre des mesures pour minimiser les déchets. Nous observons que parmi les participants, 89% sont véritablement préoccupés par le gaspillage des ressources. En revanche, seulement 4.4% des participants ne sont pas préoccupés par le gaspillage des ressources, ce qui indique une prise de conscience importante et une attitude responsable envers l'environnement. Il est également intéressant de noter que 6,7% des participants ont une attitude neutre sur la question, ce qui peut indiquer un manque de connaissance ou d'informations sur le sujet")
    
    st.markdown('<span style="color: #87CEEB;">Socially responsible person</span>', unsafe_allow_html=True)
    st.write("Cette colonne permet d’identifier les répondants qui se qualifient de socialement responsable ou pas. Nous pouvons constater que 74.2% des répondants se décrivent comme socialement responsables contre 7.8% qui affirment le contraire. 18% sont neutres.")
    
    st.markdown('<span style="color: #87CEEB;">Prefer sustainability to convenience</span>', unsafe_allow_html=True)
    st.write("Cette colonne nous informe sur la préférence des répondants. Elle mesure si la personne est prête à endurer un certain niveau d’inconfort ou de difficulté afin de prioriser les habitudes d’achat durables sur le plan environnemental. Cela implique que l’individu accorde ou pas une grande valeur à la durabilité et est prêt ou non à apporter des changements à ses habitudes d’achat afin de soutenir ses valeurs. 72,4% des répondants préfèrent la durabilité au confort contrairement à 10.2% des répondants pour qui le confort est plus important. On peut en conclure que la majorité des répondants sont enclins à préférer la durabilité au confort lors de l'achat de vêtements, bien que près de 17% des répondants ne soient pas certains de leur positionnement sur la question.")
    
    st.markdown('<span style="color: #87CEEB;">Willingness to make the world a better place</span>', unsafe_allow_html=True)
    st.write("Cette colonne démontre l’importance qu’accorde les répondants au sujet de  rendre le monde meilleur. La réponse à cette question pourrait potentiellement donner un aperçu des priorités et des motivations de la personne. Pour 93.4% des répondants cette thématique est très importante. 4.9% des répondants sont neutres et pour le reste, soit 1.7% des répondants, cela n’est pas important.")
    
    st.markdown('<span style="color: #87CEEB;">Clothing shopping frequencies</span>', unsafe_allow_html=True)
    st.write("Cette colonne mesure la fréquence d’achat de vêtements des répondants. Nous observons que la majorité des participants (40,4%) déclarent faire des achats vestimentaires une fois par mois, suivis de ceux qui achètent des vêtements tous les 3 mois (28.6%). Une petite proportion (8,2%) des participants font des achats vestimentaires chaque semaine, et 1% déclarent en acheter tous les jours. Tandis que seulement 43% disent éviter les achats vestimentaires autant que possible. En ce qui concerne les achats vestimentaires moins fréquents, 13,01% des participants déclarent faire des achats tous les 6 mois, tandis que 4,3% les font une fois par an. Les résultats montrent donc que la fréquence d'achat vestimentaire est assez variée parmi les participants de l'étude.")
    
    st.markdown('<span style="color: #87CEEB;">Own sustainable clothing</span>', unsafe_allow_html=True)
    st.write("Cette colonne permet d’identifier les répondants qui possèdent déjà des vêtements éthiques.  Nous observons que parmi les participants, 59% possèdent des vêtements durables, tandis que 6.9% n'en possèdent pas et 34.1% ne sont pas sûrs. Ces résultats suggèrent une prise de conscience croissante de l'importance de la durabilité dans l'industrie de la mode, mais aussi une incertitude quant aux caractéristiques des vêtements durables.")
    
    st.markdown('<span style="color: #87CEEB;">Well informed on sustainable clothing</span>', unsafe_allow_html=True)
    st.write("Cette colonne mesure le degré d’information des répondants par rapport à la mode éthique. 55.5% des répondants déclarent ne pas avoir assez d'informations sur le sujet. 22.7% prétendent être bien informés. Cependant 21.8% des répondants sont neutres. ")
    
    st.markdown('<span style="color: #87CEEB;">Impact of sustainable clothing on the world</span>', unsafe_allow_html=True)
    st.write("Cette colonne mesure l’impact de la mode éco responsable sur le monde. 89.8% des répondants témoignent de l’apport positif de la mode éco responsable sur le monde. Tandis que 7.9% sont neutres et 2.3% réfutent cette affirmation.")
    
    st.markdown('<span style="color: #87CEEB;">Ability to afford sustainable clothing</span>', unsafe_allow_html=True)
    st.write("Cette colonne mesure le pouvoir d’achat des répondants. Elle mesure leurs capacités à pouvoir s’acheter des vêtements éthiques. 26.3% des répondants déclarent avoir les moyens pour cela, 40.1% sont neutres et 33.6% ne peuvent pas. ")
    
    st.markdown('<span style="color: #87CEEB;">Understanding  of sustainability</span>', unsafe_allow_html=True)
    st.write("Cette colonne permet d'apprécier la définition de chaque répondant par rapport au développement durable.")
    
    st.markdown('<span style="color: #87CEEB;">Understanding of ethical fashion</span>', unsafe_allow_html=True)
    st.write("Cette colonne permet d'apprécier la définition de chaque répondant par rapport à la mode éco responsable.")
    
    st.markdown('<span style="color: #87CEEB;">Factors that influence my shopping decisions</span>', unsafe_allow_html=True)
    st.write("Cette colonne permet d’identifier les facteurs clés qui influent sur la décision d’achat des répondants.")
    
    st.markdown('<span style="color: #87CEEB;">Needs and desires</span>', unsafe_allow_html=True)
    st.write("Cette colonne permet d’identifier les attentes des consommateurs quand ils font leurs shoppings.")

    st.markdown('<span style="color: #87CEEB;">Intention to buy sustainable clothing within the next 12 months</span>', unsafe_allow_html=True)
    st.write("Cette colonne définit l’intention des répondants d’acheter des vêtements durables dans les 12 prochains mois. Nous constatons que 76.4% des répondants déclarent une intention d’acheter des vêtements durables contre 23.6% qui ne souhaitent pas en acheter. Cette colonne représente notre variable dépendante.")


if analyse_button:

    st.title('Analyse Préliminaire')
    st.markdown("<span style='color: #87CEEB;'>Relation entre le Genre et l'Intention d'Achat de la Mode Eco</span>", unsafe_allow_html=True)
    de= pd.read_csv('dataae.csv')
    # Créer le graphique en barres
    fig, ax = plt.subplots()
    ax = de[["Gender", "Intention to buy sustainable clothing within the next 12 months"]].value_counts().plot(kind="bar")

    # Calculer le total des valeurs pour afficher les pourcentages
    total = sum(de[["Gender", "Intention to buy sustainable clothing within the next 12 months"]].value_counts())

    # Créer le graphique en secteurs avec les pourcentages
    for rect in ax.patches:
     height = rect.get_height()
     ax.text(rect.get_x() + rect.get_width() / 2, height + 5, f'{height/total:.0%}', ha='center', va='bottom')

    # Personnaliser le graphique
    ax.set_title("Sustainable Clothing Purchase Intentions", loc='center')
    ax.set_xlabel("Gender")
    ax.set_ylabel("Count")

    # Afficher le graphique dans Streamlit
    st.pyplot(fig) 

    st.markdown("On peut observer que les femmes ont une intention plus élevée d'acheter des vêtements durables que les hommes, avec 68% des femmes indiquant une intention d'achat contre seulement 7% des hommes. En comparaison, 19% des femmes et 4% des hommes ont indiqué qu'ils n'ont pas l'intention d'acheter des vêtements durables dans les 12 prochains mois. En termes de pourcentage total, les femmes représentent 87% de l'échantillon tandis que les hommes représentent 11,8%.")
    
    st.markdown("<span style='color: #87CEEB;'>Relation entre l'age et l'intention d'achat de la mode eco</span>", unsafe_allow_html=True)
    figs, ax = plt.subplots()

    ax=de[["Age","Intention to buy sustainable clothing within the next 12 months"]].value_counts().plot(kind="bar")
    total = sum(de[["Age","Intention to buy sustainable clothing within the next 12 months"]].value_counts())
    for rect in ax.patches:
     height = rect.get_height()
     ax.text(rect.get_x() + rect.get_width() / 2, height + 5, f'{height/total:.0%}', ha='center', va='bottom')

     ax.set_title("Sustainable Clothing Purchase Intentions", loc='center')
     ax.set_xlabel("Age")
    ax.set_ylabel("Count")
    st.pyplot(figs) 
    
    st.markdown("La population de cette étude est majoritairement âgée entre 22 - 39 ans, de cette tranche d'âge, 48% des personnes indiquent une intention d’achat des vêtements éthique contre 20% qui indique le contraire.  20% des répondants âgés de 20 et moins sont pour cet achat contre 3% qui ne le sont pas. Nous constatons que les personnes plus âgées, c'est-à-dire de 40 ans et plus, bien que très peu représentées, montrent presque toutes une intention d’acheter la mode éthique. Juste 1% de ce groupe indique le contraire. Nous pouvons conclure que plus les gens sont âgés, plus ils tendent vers la mode éthique.")


    st.markdown("<span style='color: #87CEEB;'>Relation entre le continent de résidence et l'intention d'achat de la mode eco</span>", unsafe_allow_html=True)
    fis, ax = plt.subplots()
    ax=de[["Continent of residence","Intention to buy sustainable clothing within the next 12 months"]].value_counts().plot(kind="bar")
    total = sum(de[["Continent of residence","Intention to buy sustainable clothing within the next 12 months"]].value_counts())
    for rect in ax.patches:
     height = rect.get_height()
     ax.text(rect.get_x() + rect.get_width() / 2, height + 5, f'{height/total:.0%}', ha='center', va='bottom')

    plt.title("Sustainable Clothing Purchase Intentions")
    plt.xlabel("Continent of residence")
    plt.ylabel("Count")

    st.pyplot(fis) 
    st.markdown("En Europe, seulement 2% des répondants ne prévoient pas d'acheter de vêtements durables dans les 12 prochains mois, tandis que 19% ont l'intention d'en acheter. Cela signifie que la majorité des répondants européens sont intéressés par l'achat de vêtements durables. En Amérique du Nord, 20% des répondants ne prévoient pas d'acheter de vêtements durables dans les 12 prochains mois, tandis que 48% ont l'intention d'en acheter. Cela signifie que la majorité des répondants nord-américains sont également intéressés par l'achat de vêtements durables. L’Asie, l'Australie et l’Amérique du sud, bien que très peu représentées, indiquent tous l’intention d'émettre des achats de vêtements éthique. Cependant, 1% des répondants ressortissant de l’Asie disent le contraire. A contrario, en Afrique, tous les répondants ne souhaitent pas acheter la mode éthique. Nous pouvons en déduire que le mode consommation éthique n'est pas encore développé dans cette partie du monde.   ")

if anastat_button:
  st.title('Analyse Statistique')
  
  st.markdown("<span style='color: #87CEEB;'>Nous commençons notre analyse par un 'Describe' pour la description statistique de nos données</span>", unsafe_allow_html=True)
  from PIL import Image
  image = Image.open('describe.png')
  st.image(image, '')

  st.markdown("<span style='color: #87CEEB;'>Puis nous allons effectuer un boxplot</span>", unsafe_allow_html=True)
  from PIL import Image
  image = Image.open('boxplot.png')
  st.image(image, '')
  st.markdown("Après le topic modeling, méthode d'analyse de données qui est utilisée pour identifier les thèmes (ou sujets) dominants dans un ensemble de textes non étiquetés. Cette méthode est souvent utilisée dans le domaine de l'apprentissage automatique et du traitement du langage naturel pour extraire des informations à partir de grands volumes de données textuelles, tels que des corpus de documents ou des collections de publications en ligne. Le modèle de topic modelling est utile dans un certain nombre de domaines, tels que la recherche d'informations, l'analyse de sentiments, la veille stratégique, le marketing, la recommandation de contenu et la compréhension des opinions et des attitudes des clients. En identifiant les sujets clés présents dans les données textuelles, il est possible de comprendre les thèmes qui intéressent les gens, les problèmes qui les préoccupent, et les points de vue qu'ils expriment sur ces sujets.Nous avons effectué une analyse de Topic Modelling sur plusieurs colonnes dont: “ Understanding  of sustainability”, “Understanding of ethical fashion”, “Factors that influence my shopping decisions”, et “Needs and desires”. Le processus consistait à nettoyer le texte en utilisant la tokenisation, l'enlèvement des stop words et la lemmatisation. Ensuite, créer une matrice de document-termes, qui a été utilisée pour entraîner un modèle de Topic Modelling à l'aide de la bibliothèque Gensim. Nous avons choisi d'avoir 3 sujets pour notre modèle et avons effectué 30 passes pour entraîner le modèle.")
  st.markdown("<span style='color: #87CEEB;'>Analyse PCA</span>", unsafe_allow_html=True)
  image = Image.open('PCA.png')
  st.image(image, '')
  st.write(" D'apres le critère de Kaiser, on peut prendre tous les PCA qui ont une inertie supérieure ou égal à 5.26%. Nous pouvons donc prendre les 7 premiers PCA; c'est à dire PC1 à PC7. Cela nous donnera un degré d'importance cummulé de 82.01%")
  st.write(" Modèle de classification: KMEANS & LOGISTIC REGRESSION ")
  st.markdown("<span style='color: #87CEEB;'>Elbow Method</span>", unsafe_allow_html=True)
  image = Image.open('Em.png')
  st.image(image, '')
  st.markdown("<span style='color: #87CEEB;'>KMEANS</span>", unsafe_allow_html=True)
  image = Image.open('KMEANS.png')
  st.image(image, '')
  st.markdown("Nous avons développé un modèle de classification K Means. Ce modèle a divisé notre population en deux groupes (Classe A et Classe B). La classe A représente une population “pas responsable”. La classe B représente une population “responsable”.")
  st.markdown("<span style='color: #87CEEB;'>Les caractéristiques de la Classe A</span>", unsafe_allow_html=True)
  image = Image.open('GROUPEA.png')
  st.image(image, '')
  st.markdown("La classe A représente la population que nous pouvons décrire de pas socialement responsable. En effet, la classe A regroupe des personnes qui ne se considèrent pas socialement responsables à hauteur de 61%, et 27,9% ont une position neutre à ce sujet. De plus, 84.5% de cette population soit, privilégie leur confort personnel plutôt que le développement durable ou ont une position neutre. Sans oublier que plus de la moitié (53,5%) de cette population ne possède aucun vêtement durable.")

  st.markdown("<span style='color: #87CEEB;'>Les caractéristiques de la Classe B</span>", unsafe_allow_html=True)
  image = Image.open('GROUPEB.png')
  st.image(image, '')
  st.markdown("La population de la classe B est caractérisée par une forte responsabilité sociale. En effet, 90% de cette population s'identifient comme étant socialement responsables. De plus, 89,6% de cette population sont prêts à faire des choix inconfortables s'ils ont un impact positif sur l'environnement. Et bien évidemment, 67.1% de cette population sont propriétaires de vêtements éco responsables.")
  
  image = Image.open('mdc.png')
  st.image(image, '')
  st.markdown("Nous avons ensuite créé un modèle d’apprentissage de régression logistique. La régression logistique est un algorithme d'apprentissage supervisé utilisé pour prédire une variable binaire ou catégorielle en fonction d'un ensemble de variables prédictives. La régression logistique est largement utilisée dans divers domaines, tels que l'analyse de données, l'apprentissage automatique et la science des données. Elle est particulièrement utile lorsque la variable cible est binaire, par exemple, pour prédire si un client achètera ou non un produit. Ce modèle nous permettra de prédire l’intention d’acheter des vêtements durables. Ceux qui sont susceptibles d’acheter des vêtements éthique sont représentés par des 1 et le groupe opposé par des 0. Nous avons choisi ce modèle pour plusieurs raisons. Premièrement, nos données sont du type objet et donc la régression logistique est plus adaptée pour ce type de donnée. De plus, il n'est pas nécessaire que la variable dépendante et les variables explicatives soient fortement corrélées dans le cas de la régression logistique. La régression logistique est utilisée pour modéliser la relation entre les variables prédictives et la probabilité de la variable dépendante appartenant à une classe donnée. Ainsi, même si les variables explicatives et la variable dépendante ne sont pas fortement corrélées, la régression logistique peut encore capturer les relations non linéaires ou complexes entre les variables. Compte tenu de nos données, ce modèle d'apprentissage est recommandé. Le score obtenu pour le modèle de régression logistique sur l'ensemble d'entraînement est de 0.823, ce qui signifie que le modèle a correctement classé 82.3% des échantillons d'entraînement. Le score obtenu pour l'ensemble de test est de 0.81, ce qui signifie que le modèle a correctement classé 81% des échantillons de test.Le résultat de la matrice de confusion (cm) montre que le modèle a classé 66 échantillons comme étant de la classe 0 et qui étaient effectivement de la classe 0. Il a également classé 89 échantillons comme étant de la classe 1 alors qu'ils étaient en réalité de la classe 0. D'autre part, il a classé 35 échantillons comme étant de la classe 0 alors qu'ils étaient en réalité de la classe 1, et il a correctement classé 463 échantillons comme étant de la classe 1. Ainsi, on peut dire que le modèle a de meilleures performances pour la classe 1, avec une classification correcte de 463 échantillons sur les 498 échantillons de cette classe dans l'ensemble de test. Cependant, le modèle a des difficultés à classer les échantillons de la classe 0, avec une classification correcte de seulement 66 échantillons sur les 155 échantillons de cette classe dans l'ensemble de test.")
  image = Image.open('mdcpl.png')
  st.image(image, '')
  
  st.markdown("<span style='color: #87CEEB;'>Interprétation</span>", unsafe_allow_html=True)
  st.write("L’objectif de cette recherche est de contribuer au changement dans le mode de consommation vers une mode plus éthique et responsable. Grâce à nos différents modèles d'apprentissage, nous avons pu identifier différentes barrières à ce mouvement. Ainsi nous pourrons utiliser ces informations pour créer des stratégies innovantes pour atteindre notre objectif. ")

if barr_button:
  st.title("Les barrières au changement de mode de consommation")
  st.markdown("La mode éthique à ce jour n’a pas de définition « simple », on parle plutôt d’une pratique. Le journal des ateliers Lemahieu définit la mode éthique comme la volonté de limiter l’impact sur la planète au quotidien mais également sur les êtres humains, partie prenante de la chaîne de fabrication. La mode éthique est une alternative à la fast fashion. Elle vise à proposer des vêtements plus respectueux des hommes et de l’environnement. Cela passe par le choix des matières, les lieux de production, mais aussi le processus de fabrication.  Les résultats du topic modelling démontrent que nos répondants ont bien compris le sujet de l'étude. Cependant, cette étude démontre aussi que la majorité de la population n’ont pas de plus ample information sur cette thématique.  Plus de la moitié des répondants déclarent ne pas être bien informés sur ce sujet. Lorsqu'une grande partie de la population manque d'informations sur une question donnée, cela peut affecter leur capacité à prendre des décisions éclairées. De plus, lorsque les individus ne sont pas bien informés sur un sujet, ils deviennent plus vulnérables à la manipulation et à la désinformation. Cela est donc un frein au changement que nous voulons obtenir. Notre modèle de topic modelling nous a aussi permis de mettre en évidence les besoins des consommateurs. Un besoin assez criant est que les consommateurs recherchent des vêtements durables et de qualité mais à des prix abordables. Cette demande croissante pour des produits durables reflète une préoccupation croissante pour l'environnement, l'éthique et la durabilité. La preuve c’est que  pour 93.4% des répondants, rendre le monde meilleur pour y vivre est très important. Cependant, les vêtements durables ont tendance à être plus chers que les vêtements conventionnels de qualité inférieure. Il y a donc un défi à concilier ces attentes contradictoires de durabilité, de qualité et de prix abordable. Afin d’amener un changement dans la consommation vers la mode éthique, nous devons trouver des solutions innovantes pour répondre à cette demande des consommateurs. Selon notre modèle de classification, les personnes “pas socialement responsables” privilégient leur confort personnel au développement durable. Cela peut s’expliquer par le manque de sensibilisation. Certaines personnes peuvent ne pas être pleinement conscientes des enjeux liés au développement durable, de leurs conséquences à long terme et de l'importance de prendre des mesures responsables. Les habitudes et modes de vie établis peuvent aussi être une raison à ce phénomène.  Les habitudes et les modes de vie établis sont souvent difficiles à changer. Si une personne est habituée à un certain niveau de confort et de consommation, il peut être difficile de remettre en question ces comportements et de faire des choix plus durables qui pourraient nécessiter des ajustements et des efforts supplémentaires. Cela nous montre que la sensibilisation, l'éducation et la promotion de modes de vie durables peuvent jouer un rôle clé pour encourager davantage de personnes à adopter des comportements responsables. Aussi, selon notre modèle de classification, les personnes “pas socialement responsables”  ne se considèrent pas socialement responsables. Il convient de noter que l'auto-évaluation de la responsabilité sociale peut être subjective et varier d'une personne à l'autre. Il y a plusieurs raisons pour lesquelles une personne peut s'auto-évaluer comme étant 'pas responsable' d'un point de vue social. Premièrement, un manque de conscience sociale. En effet, certaines personnes peuvent ne pas être conscientes des enjeux sociaux et de leur responsabilité envers la société. Elles peuvent ne pas avoir été exposées à des valeurs sociales importantes ou n'ont pas été sensibilisées aux problèmes auxquels font face certaines communautés ou la planète dans son ensemble. Par ailleurs, les priorités personnelles sont différentes. Chaque individu a ses propres priorités et valeurs. Certaines personnes peuvent accorder plus d'importance à des aspects individuels, tels que la réussite professionnelle ou financière, plutôt qu'à des engagements sociaux. Elles peuvent considérer que leurs responsabilités se limitent à leur propre cercle familial ou à leur propre réussite personnelle. Une autre raison peut être l’ignorance ou désinformation. Une personne peut manquer de connaissances ou être mal informée sur les problèmes sociaux et les bonnes pratiques de responsabilité sociale. Cela peut conduire à des comportements qui ne tiennent pas compte des conséquences négatives sur la société. ")
