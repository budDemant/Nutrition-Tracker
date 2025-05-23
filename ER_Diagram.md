```mermaid
erDiagram
    USERS {
        int id PK
        string email -- unique
        string username -- unique
        string password
    }
    FOODS {
        int id PK
        string name
        float serving_size
        string unit 
    }
    FOODLOGS {
        int id PK
        int user_id FK
        int food_id FK
        date datetime
        float servings
    }
    NUTRIENTS {
        int id PK
        string name
        string unit
        string nutrient_number
    }
    FOODNUTRIENTS {
        int id PK
        int food_id FK
        int nutrient_id FK
        float amount_per_serving
    }
    GOALS {
        int id PK
        int user_id FK
        int nutrient_id FK
        float target_value
        string unit
        string type

    }
    USERS ||--o{ FOODLOGS : logs
    FOODS ||--o{ FOODLOGS : is_logged_in
    USERS ||--o{ GOALS : sets
    NUTRIENTS ||--o{ GOALS : for
```