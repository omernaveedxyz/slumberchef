import { column, defineDb, defineTable } from "astro:db";

const Ingredient = defineTable({
  columns: {
    id: column.number({ primaryKey: true }),
    name: column.text({ unique: true }),
    strength: column.number(),
  },
});

const Dish = defineTable({
  columns: {
    id: column.number({ primaryKey: true }),
    name: column.text({ unique: true }),
    type: column.text(),
    baseStrength: column.number(),
    minPotSize: column.number(),
  },
});

const DishIngredient = defineTable({
  columns: {
    dishId: column.number({ references: () => Dish.columns.id }),
    ingredientId: column.number({ references: () => Ingredient.columns.id }),
    quantity: column.number(),
  },
});

// https://astro.build/db/config
export default defineDb({
  tables: { Ingredient, Dish, DishIngredient },
});
