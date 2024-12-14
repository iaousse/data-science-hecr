# Big data & cloud computing

Le Big Data est un terme qui désigne des ensembles de données extrêmement volumineux, diversifiés et générés à un rythme rapide. Avec l’évolution des technologies numériques, ces données, issues de sources variées et souvent non structurées, sont devenues une ressource cruciale pour les organisations modernes. Contrairement aux ensembles de données traditionnels, qui sont souvent structurés et d’une taille raisonnable, le Big Data peut englober des données provenant de capteurs, de réseaux sociaux, de transactions commerciales et même de sources non conventionnelles comme les vidéos ou les images. En analysant ces données, les entreprises et les institutions peuvent obtenir des insights précieux pour prendre des décisions éclairées, anticiper des tendances et améliorer leurs performances. Ce phénomène s’intègre de manière fondamentale dans de nombreux secteurs, notamment la finance, la santé, le marketing, et même les gouvernements, qui utilisent le Big Data pour optimiser leurs services et renforcer leur efficacité.

Historiquement, l’essor du Big Data a suivi la montée en puissance d’Internet et de l’informatique. À la fin des années 1990 et au début des années 2000, avec l'augmentation rapide de la capacité de stockage numérique, les entreprises ont commencé à accumuler d’énormes quantités de données. Cependant, les outils traditionnels de gestion et d’analyse de données, tels que les bases de données relationnelles, ont rapidement montré leurs limites face à ce volume grandissant. La création de nouveaux systèmes, comme le Hadoop Distributed File System (HDFS) et le modèle MapReduce, a marqué une étape cruciale dans le traitement et le stockage des données massives. Ces systèmes permettent de distribuer les données sur plusieurs machines et de traiter des tâches en parallèle, rendant l’analyse de grandes quantités de données plus rapide et plus efficace.

Les méthodes traditionnelles de traitement de données, conçues pour des données structurées et de taille limitée, ne peuvent pas répondre aux besoins actuels du Big Data. Les bases de données relationnelles, par exemple, sont souvent lentes et peu adaptées au stockage de données non structurées telles que des images, des vidéos ou des textes provenant de sources variées. De plus, ces méthodes ne permettent pas de traiter en temps réel des flux de données rapides, comme ceux produits par les appareils connectés ou les réseaux sociaux. Dans un monde où chaque seconde produit une quantité massive de nouvelles données, les systèmes de traitement traditionnels sont incapables de fournir des résultats rapidement et efficacement. En revanche, les technologies modernes de Big Data, avec leurs capacités de traitement parallèle et leur flexibilité dans le traitement de données variées, permettent de relever ces défis.

Le Big Data se caractérise par plusieurs attributs clés, souvent appelés les "V" du Big Data : Volume, Variété, Vélocité, Véracité et Valeur. 


## Les Principes Fondamentaux du Big Data

### Les Caractéristiques du Big Data (les "V" du Big Data)

#### Volume

```{admonition} Définition
Le volume désigne la quantité massive de données générées et collectées par les entreprises, les appareils connectés, les réseaux sociaux, et de nombreuses autres sources. Ces données peuvent atteindre des téraoctets, des pétaoctets, voire des exaoctets.
```

Le volume des données disponibles augmente de façon exponentielle, principalement dû à l'Internet des Objets (IoT), aux réseaux sociaux, et à la numérisation des processus. Par exemple, les plateformes de streaming vidéo et les réseaux sociaux génèrent chaque jour des quantités astronomiques de données, qu'il serait impossible de traiter et d'analyser avec des méthodes traditionnelles.

```{admonition} Exemple
Un exemple concret est celui de Facebook, qui collecte des données sur chaque interaction des utilisateurs avec ses contenus (likes, partages, commentaires). Ces données, lorsqu’elles sont agrégées, permettent à l’entreprise de mieux comprendre les comportements et les préférences de ses utilisateurs.
```

#### Variété

```{admonition} Définition
La variété se réfère à la diversité des types de données collectées, qu'il s'agisse de données structurées (bases de données relationnelles), semi-structurées (fichiers XML, JSON) ou non structurées (images, vidéos, messages sur les réseaux sociaux).
```

La diversité des sources de données et des formats rend l’analyse plus complexe mais également plus riche. Les données textuelles issues des réseaux sociaux, les images de vidéosurveillance, les données de capteurs et même les transactions financières sont toutes des types de données que les entreprises doivent intégrer pour obtenir une vision complète de leurs activités.

```{admonition} Exemple
Dans le domaine de la santé, les hôpitaux génèrent des données variées, incluant des dossiers médicaux électroniques (données structurées), des images médicales (données non structurées), et des notes de médecins (données semi-structurées). Ces différentes formes de données permettent d’enrichir les analyses pour améliorer les diagnostics et les traitements.
```

#### Vélocité

```{admonition} Définition
La vélocité indique la vitesse à laquelle les données sont générées et doivent être traitées. Dans un environnement de Big Data, les données sont souvent produites en continu et en temps réel.
```

La vitesse de génération des données est un défi majeur dans le Big Data. L’ère du numérique exige que ces données soient traitées et analysées en temps réel pour que les entreprises puissent répondre rapidement aux changements de marché et aux besoins des clients. Par exemple, les bourses de valeurs traitent des millions de transactions par seconde, nécessitant une infrastructure capable de gérer cette vélocité.

```{admonition} Exemple
Dans l'industrie des services financiers, la détection de fraude en temps réel est essentielle. Les transactions doivent être analysées immédiatement pour identifier des comportements suspects avant qu'une fraude ne se produise, ce qui nécessite un traitement des données à très haute vélocité.
```

#### Véracité

```{admonition} Définition
La véracité fait référence à la qualité et à la fiabilité des données. Les données collectées doivent être précises, cohérentes, complètes, et sans ambiguïté pour être utiles dans les analyses.
```

La véracité est particulièrement critique, car des données de mauvaise qualité peuvent fausser les analyses et mener à des décisions erronées. Les organisations investissent donc dans des processus de nettoyage et de validation des données pour s’assurer que leurs analyses reposent sur des informations fiables.

```{admonition} Exemple
Dans le domaine de la logistique, des données imprécises sur les stocks peuvent entraîner des ruptures de stock ou des surcharges d’inventaire. La véracité des données est donc cruciale pour optimiser la gestion des stocks et la satisfaction des clients.
```

#### Valeur

```{admonition} Définition
La valeur est le bénéfice potentiel que les organisations peuvent tirer de l'analyse des données pour générer des insights pertinents et soutenant la prise de décision.
```

Le but ultime du Big Data est de transformer ces vastes quantités de données en informations exploitables pour l’entreprise. La valeur de ces données est souvent révélée par des analyses qui peuvent, par exemple, aider à anticiper les tendances du marché, personnaliser les services clients, et optimiser les processus.

```{admonition} Exemple
Dans le commerce de détail, les analyses de données permettent d’optimiser les promotions et de personnaliser les offres pour chaque client, augmentant ainsi la satisfaction client et les revenus. 
```




### Technologies et Infrastructures de Big Data

Avec l’émergence du Big Data, de nouvelles technologies et infrastructures ont été développées pour répondre aux défis posés par le volume, la diversité et la vélocité des données. Les systèmes traditionnels n'étant plus capables de traiter efficacement des ensembles de données massifs et complexes, des plateformes spécialisées ont vu le jour, parmi lesquelles Hadoop et son écosystème occupent une place centrale. Cette section examine les principales technologies et infrastructures qui ont permis le développement et l'implémentation de solutions Big Data.

#### Hadoop et son importance

```{admonition} Définition
Hadoop est une plateforme open-source de stockage et de traitement de données massives en mode distribué. Il a été développé pour permettre aux organisations de traiter et analyser de grandes quantités de données de manière rapide, fiable et économique.
```

Hadoop est devenu la technologie de référence pour le Big Data, grâce à sa capacité à distribuer des données et des traitements sur un grand nombre de machines, ce qui permet d’obtenir des résultats rapidement sans nécessiter de superordinateurs coûteux. Il repose sur deux principaux composants : le Hadoop Distributed File System (HDFS) pour le stockage distribué et le modèle de programmation MapReduce pour le traitement des données. Ensemble, ils permettent de diviser les tâches en plusieurs sous-tâches et de les exécuter en parallèle, réduisant ainsi le temps de traitement.

```{admonition} Exemple
Dans le secteur de l'e-commerce, Hadoop est utilisé pour analyser le comportement d'achat des utilisateurs en temps quasi réel, en traitant des millions de transactions et d’interactions chaque jour. Les données sont distribuées et analysées rapidement, ce qui permet aux entreprises de comprendre les tendances et de proposer des recommandations de produits personnalisées.
```

#### Hadoop Distributed File System (HDFS)

```{admonition} Définition
Hadoop Distributed File System (HDFS) est le système de fichiers distribué de Hadoop. Il permet de stocker des fichiers volumineux en les divisant en blocs, puis en les répliquant sur plusieurs nœuds du cluster, assurant ainsi la disponibilité et la tolérance aux pannes.
```

HDFS est essentiel pour la fiabilité et la scalabilité de Hadoop. Chaque fichier est fragmenté en blocs de données et chaque bloc est copié sur plusieurs nœuds du cluster. En cas de défaillance d’un nœud, les données restent accessibles à partir d’autres nœuds, garantissant ainsi la continuité des opérations sans interruption. Cette architecture permet également de gérer des données de grande taille sans nécessiter d'infrastructures complexes.

```{admonition} Exemple
Par exemple, un moteur de recherche peut utiliser HDFS pour stocker et indexer des pages web provenant de sources multiples. En cas de défaillance d’un serveur, HDFS continue de fournir les données via les copies répliquées sur d’autres serveurs, maintenant ainsi la disponibilité du système.
```

#### Clusters de Big Data et leur rôle

```{admonition} Définition
Un cluster de Big Data est un ensemble de machines interconnectées qui travaillent ensemble pour stocker, gérer et analyser de grandes quantités de données. Chaque machine, ou nœud, exécute une partie de la tâche globale, ce qui permet de diviser la charge de travail et d'accélérer le traitement des données.
```

Les clusters sont une infrastructure clé dans les environnements Big Data, car ils permettent de gérer des volumes de données énormes en utilisant des ressources matérielles et logicielles distribuées. Dans un cluster, chaque nœud exécute une partie des calculs, et l’ensemble des résultats est ensuite agrégé pour fournir une réponse rapide et précise. L’architecture des clusters facilite également la montée en charge : si les données ou les exigences de traitement augmentent, il est possible d’ajouter des nœuds supplémentaires pour augmenter la capacité.

```{admonition} Exemple
Dans le domaine de la recherche scientifique, les clusters de Big Data sont utilisés pour analyser des ensembles de données massifs provenant de simulations, de relevés climatiques ou d’études génomiques. La répartition des tâches entre plusieurs nœuds permet d’accélérer considérablement le temps de calcul.
```

#### Commodity Hardware et infrastructures de stockage

```{admonition} Définition
Le terme "commodity hardware" désigne du matériel standard, facilement accessible et bon marché, utilisé dans les clusters de Big Data pour le stockage et le traitement des données. Contrairement aux systèmes de stockage spécialisés, le commodity hardware permet de réduire les coûts sans compromettre la performance.
```

L’un des principes fondamentaux du Big Data est de tirer parti de matériel économique, sans investir dans des serveurs coûteux. En utilisant des composants standards, tels que des disques durs classiques et des processeurs ordinaires, les organisations peuvent construire des infrastructures de stockage et de traitement de données à grande échelle tout en maîtrisant les coûts. Les logiciels comme Hadoop sont conçus pour fonctionner efficacement sur ce type de matériel, en assurant la gestion des pannes et la redondance des données.

```{admonition} Exemple
Les grandes entreprises de technologie, comme Facebook et Twitter, utilisent des infrastructures basées sur du commodity hardware pour stocker et traiter les données de leurs utilisateurs. Ces infrastructures permettent de maintenir des coûts raisonnables tout en répondant aux besoins de traitement massif des données.
```

### Algorithmes et Traitement des Données

Les algorithmes et les méthodes de traitement des données sont au cœur de la gestion du Big Data. Dans les environnements de Big Data, les approches traditionnelles de traitement en série ne sont pas efficaces pour traiter les volumes massifs de données. Des algorithmes et des méthodes spécifiques, tels que MapReduce, la réplication des données et le spilling to disk, permettent d'optimiser le traitement et de garantir la disponibilité des données, même en cas de contraintes de ressources.

#### MapReduce : Processus Map et Reduce

```{admonition} Définition
MapReduce est un modèle de programmation développé pour traiter de grandes quantités de données en parallèle. Il se compose de deux étapes principales : le processus Map, qui divise la tâche en sous-tâches traitées individuellement, et le processus Reduce, qui agrège les résultats pour produire une sortie finale.
```

Le modèle MapReduce est conçu pour fonctionner efficacement dans un environnement distribué, où chaque nœud d’un cluster peut exécuter des parties de l'algorithme en parallèle. Dans le processus **Map**, les données sont d'abord divisées et traitées indépendamment, ce qui permet une distribution de la charge de travail. Ensuite, dans le processus **Reduce**, les résultats partiels des différentes étapes Map sont combinés pour obtenir le résultat global. Cette approche permet de traiter des volumes massifs de données de manière efficace, en exploitant la puissance de traitement parallèle des clusters.

```{admonition} Exemple
Pour une entreprise de vente en ligne, MapReduce peut être utilisé pour analyser des millions de transactions afin de détecter des tendances d'achat. Le processus Map pourrait extraire et comptabiliser les achats par catégorie de produit, et le processus Reduce pourrait combiner ces résultats pour identifier les produits les plus populaires par région et par saison.
```

#### Réplication des données

```{admonition} Définition
La réplication des données est une méthode qui consiste à dupliquer les données sur plusieurs nœuds d'un cluster. Cette technique permet d'assurer la durabilité et la disponibilité des données en cas de panne d’un nœud, garantissant ainsi que les données restent accessibles même dans des environnements à haute tolérance aux pannes.
```

Dans un système de Big Data, la perte de données ou l'interruption du service est souvent inacceptable, surtout dans les secteurs où la continuité des opérations est essentielle. La réplication permet de conserver des copies des données sur plusieurs nœuds d'un cluster. En cas de panne ou de dysfonctionnement d'un nœud, les autres nœuds du cluster peuvent prendre le relais, évitant ainsi les pertes de données. Cette redondance est une composante essentielle pour les infrastructures de Big Data, qui doivent être à la fois robustes et résilientes.

```{admonition} Exemple
Dans les systèmes de banque en ligne, la réplication des données assure que les informations des comptes clients soient toujours disponibles, même si un serveur de données tombe en panne. Cette redondance garantit que les clients peuvent accéder à leurs informations en tout temps sans interruption de service.
```

#### Spilling to Disk pour la gestion des ressources

```{admonition} Définition
Le spilling to disk est une technique utilisée pour gérer les situations où la mémoire vive (RAM) disponible est insuffisante pour traiter un ensemble de données. Lorsqu'un programme de traitement de données manque de mémoire, il déplace temporairement les données vers le disque dur, permettant de continuer le traitement sans interruption.
```

Dans un environnement Big Data, la taille des données dépasse souvent la capacité de la mémoire vive, surtout lorsque des calculs complexes sont effectués. Le spilling to disk permet de pallier cette limitation en utilisant l'espace disque comme mémoire auxiliaire. Bien que cela entraîne une certaine lenteur par rapport au traitement en mémoire, cette technique est essentielle pour traiter des ensembles de données de grande taille avec des ressources limitées.

```{admonition} Exemple
Dans le cadre d'une analyse de données massives, si un programme de tri des données dépasse la capacité de la mémoire, le spilling to disk permet de stocker temporairement des parties de données sur le disque pour terminer le tri. Cette technique est couramment utilisée dans les systèmes de traitement de Big Data pour éviter les erreurs de dépassement de mémoire.
```




