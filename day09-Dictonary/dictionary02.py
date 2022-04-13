# Nesting

capitals = {'France': 'Paris', 'Spain': 'Madrid', 'United Kingdom': 'London' }

# Nesting a List within a Dictionary

travel_plans = {'France': ['Paris', 'Lyon', 'Marseille'],
                'Spain': ['Madrid', 'Barcelona', 'Valencia'],
                'United Kingdom': ['London', 'Birmingham', 'Glasgow']}

# Nesting a Dictionary within a Dictionary

travel_plans = {'France': {'capital': 'Paris', 'cities': ['Paris', 'Lyon', 'Marseille']},
                'Spain': {'capital': 'Madrid', 'cities': ['Madrid', 'Barcelona', 'Valencia']},
                'United Kingdom': {'capital': 'London', 'cities': ['London', 'Birmingham', 'Glasgow']}}

# Nesting a Dictionary within a List

travel_plans = [
    {'country': 'France', 
     'capital': 'Paris', 
     'cities': ['Paris', 'Lyon', 'Marseille']
    },
    {'country': 'Spain', 
     'capital': 'Madrid', 
     'cities': ['Madrid', 'Barcelona', 'Valencia']
    },
    {'country': 'United Kingdom',
     'capital': 'London', 
     'cities': ['London', 'Birmingham', 'Glasgow']
    }
]
