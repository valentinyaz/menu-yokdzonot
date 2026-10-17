// ============================================================
//  MENÚ DEL CENOTE YOKDZONOT
//  Este es el ÚNICO archivo que hay que editar para cambiar
//  precios, platillos, descripciones o fotos.
//
//  - nombre / desc:  { es: "...", en: "..." }  (o un texto si es igual en ambos)
//  - precio:         número en pesos (MXN)
//  - precios:        [vaso, jarra] cuando el grupo tiene "columnas"
//  - foto:           "fotos/archivo.jpg"  (opcional)
//  - etiqueta:       { es, en } pequeña insignia (opcional)
//  - agotado: true   lo muestra tachado como "Agotado hoy" (opcional)
// ============================================================

window.MENU = {
  restaurante: {
    nombre: "Cenote Yokdzonot",
    lugar: "Yokdzonot, Yucatán",
    lema: {
      es: "Cocina yucateca a la orilla del cenote",
      en: "Yucatecan cooking by the cenote",
    },
  },

  // Deja "" para ocultar cualquiera de estos datos
  contacto: {
    horario: { es: "", en: "" },
    whatsapp: "", // ej. "529991234567"
    mapa: "", // enlace de Google Maps
  },

  secciones: [
    {
      id: "entradas",
      conFotos: true, // muestra "Foto próximamente" en platillos sin foto
      titulo: { es: "Entradas", en: "Starters" },
      grupos: [
        {
          items: [
            { nombre: "Nachos", precio: 130, desc: { es: "Totopos crujientes", en: "Crispy tortilla chips" } },
            {
              nombre: { es: "Nachos con pollo", en: "Chicken nachos" },
              foto: "fotos/nachos-con-pollo.jpg",
              precio: 150,
              desc: { es: "Totopos con pollo", en: "Tortilla chips with chicken" },
            },
            {
              nombre: { es: "Salsa Zikilpac", en: "Zikilpac dip" },
              foto: "fotos/salsa-zikilpac.jpg",
              precio: 140,
              etiqueta: { es: "Receta regional", en: "Regional recipe" },
              desc: {
                es: "Tomate asado con pepita de calabaza, una receta regional realmente deliciosa, con totopos",
                en: "Roasted tomato and pumpkin seed dip, a truly delicious regional recipe, served with tortilla chips",
              },
            },
            { nombre: "Guacamole", precio: 140, foto: "fotos/guacamole.jpg" },
            { nombre: { es: "Postre del día", en: "Dessert of the day" }, precio: 60 },
          ],
        },
      ],
    },

    {
      id: "antojitos",
      conFotos: true,
      titulo: { es: "Antojitos", en: "Antojitos" },
      nota: { es: "Órdenes de 3 piezas", en: "Orders of 3 pieces" },
      grupos: [
        {
          items: [
            {
              nombre: "Panuchos",
              foto: "fotos/panuchos.jpg",
              precio: 120,
              etiqueta: { es: "Clásico yucateco", en: "Yucatán classic" },
              desc: {
                es: "Tortilla hecha a mano rellena de frijol con lechuga, pollo, tomate y cebolla",
                en: "Handmade tortilla stuffed with bean paste, topped with lettuce, chicken, tomato and onion",
              },
            },
            {
              nombre: "Salbutes",
              foto: "fotos/salbutes.jpg",
              precio: 120,
              desc: {
                es: "Tortilla cocida en aceite con lechuga, pollo, tomate y cebolla",
                en: "Handmade puffed fried tortilla topped with chicken, lettuce, tomato and onion",
              },
            },
            {
              nombre: "Empanadas",
              foto: "fotos/empanadas.jpg",
              precio: 120,
              desc: {
                es: "Tortilla doblada con queso o pollo, lechuga, salsa de tomate y crema",
                en: "Handmade tortilla folded over cheese or chicken, topped with lettuce, tomato sauce and cream",
              },
            },
            {
              nombre: "Quesadillas",
              foto: "fotos/quesadillas.jpg",
              precio: 130,
              desc: {
                es: "Tortilla de harina con jamón y queso, lechuga, salsa de tomate y crema",
                en: "Flour tortilla with ham and cheese, lettuce, tomato sauce and cream",
              },
            },
            {
              nombre: "Sopes",
              foto: "fotos/sopes.jpg",
              precio: 130,
              desc: {
                es: "Tortilla cocida en comal con frijol, queso, lechuga, pollo y salsa de tomate",
                en: "Tortilla cooked on a traditional comal, topped with bean paste, cheese, lettuce, chicken and tomato sauce",
              },
            },
          ],
        },
      ],
    },

    {
      id: "especialidades",
      conFotos: true,
      titulo: { es: "Especialidades", en: "Specialties" },
      grupos: [
        {
          items: [
            {
              nombre: "Poc Chuc",
              foto: "fotos/poc-chuc.jpg",
              precio: 180,
              etiqueta: { es: "El favorito", en: "House favorite" },
              desc: {
                es: "Cerdo asado con arroz, frijol, cebolla, salsa de tomate y tortillas hechas a mano",
                en: "Grilled pork with rice, bean paste, onion, tomato sauce and handmade tortillas",
              },
            },
            {
              nombre: { es: "Pechuga de pollo a la plancha", en: "Grilled chicken breast" },
              foto: "fotos/pechuga-a-la-plancha.jpg",
              precio: 180,
              desc: {
                es: "Con arroz, frijol, salsa de tomate y tortillas hechas a mano",
                en: "With rice, bean paste, tomato sauce and handmade tortillas",
              },
            },
            {
              nombre: { es: "Empanizado de pollo o puerco", en: "Breaded chicken or pork" },
              foto: "fotos/empanizado.jpg",
              precio: 190,
              desc: {
                es: "Con arroz, frijol y tortillas hechas a mano",
                en: "With rice, bean paste and handmade tortillas",
              },
            },
            {
              nombre: { es: "Menú vegetariano", en: "Vegetarian plate" },
              foto: "fotos/menu-vegetariano.jpg",
              precio: 180,
              etiqueta: { es: "Vegetariano", en: "Vegetarian" },
              desc: {
                es: "Soufflé de verduras: capas de verduras con queso fundido, crema y pan molido. Con arroz, frijol, ensalada y tortillas hechas a mano",
                en: "Vegetable soufflé: layers of vegetables with melted cheese, cream and breadcrumbs. With rice, bean paste, salad and handmade tortillas",
              },
            },
            {
              nombre: { es: "Ensalada Yokdzonot", en: "Yokdzonot salad" },
              foto: "fotos/ensalada-yokdzonot.jpg",
              precio: 180,
              etiqueta: { es: "De la casa", en: "House salad" },
              desc: {
                es: "Lechuga, jitomate y cebolla con puerco o pollo. Sana y deliciosa",
                en: "Lettuce, tomato and onion with chicken or pork. Fresh and delicious",
              },
            },
            {
              nombre: { es: "Fajitas de pollo", en: "Chicken fajitas" },
              foto: "fotos/fajitas-de-pollo.jpg",
              precio: 190,
              desc: {
                es: "Pechuga de pollo con arroz, frijol y tortillas hechas a mano",
                en: "Chicken breast with rice, bean paste and handmade tortillas",
              },
            },
            {
              nombre: { es: "Sopa de lima", en: "Lime soup" },
              precio: 100,
              desc: {
                es: "Caldo tradicional yucateco de pollo con lima y tiras de tortilla",
                en: "Traditional Yucatecan chicken broth with local lime and tortilla strips",
              },
            },
          ],
        },
      ],
    },

    {
      id: "bebidas",
      titulo: { es: "Bebidas", en: "Drinks" },
      grupos: [
        {
          titulo: { es: "Aguas frescas", en: "Fresh fruit waters" },
          columnas: [
            { es: "Vaso", en: "Glass" },
            { es: "Jarra", en: "Pitcher" },
          ],
          items: [
            { nombre: { es: "Limonada mineral", en: "Sparkling lemonade" }, precios: [50, 140] },
            { nombre: "Horchata", precios: [40, 120] },
            { nombre: { es: "Jamaica", en: "Hibiscus" }, precios: [40, 120] },
            { nombre: { es: "Chaya con piña", en: "Chaya & pineapple" }, precios: [50, 130] },
            { nombre: { es: "Chaya con limón", en: "Chaya & lime" }, precios: [50, 130] },
            { nombre: { es: "Limonada", en: "Lemonade" }, precios: [40, 120] },
          ],
        },
        {
          titulo: { es: "Café y té", en: "Coffee & tea" },
          items: [
            { nombre: "Nescafé", precio: 40 },
            { nombre: { es: "Café americano", en: "Americano" }, precio: 40 },
            { nombre: { es: "Café con leche", en: "Coffee with milk" }, precio: 50 },
            { nombre: { es: "Té de manzanilla", en: "Chamomile tea" }, precio: 40 },
            { nombre: "Espresso", precio: 60 },
          ],
        },
        {
          titulo: { es: "Especialidades de la casa", en: "House cocktails" },
          items: [
            { nombre: "Margarita", precio: 110 },
            { nombre: "Piña colada", precio: 110 },
            { nombre: "Tequila sunrise", precio: 100 },
            { nombre: "Tequila", precio: 70 },
            { nombre: "Tequila Don Julio", precio: 110 },
            { nombre: { es: "Vino tinto", en: "Red wine" }, precio: 100 },
            { nombre: { es: "Vino blanco", en: "White wine" }, precio: 100 },
            { nombre: "Daiquiri", precio: 100 },
            { nombre: "Sangría", precio: 110 },
            { nombre: "Cuba libre", precio: 100 },
          ],
        },
        {
          titulo: { es: "Cervezas", en: "Beers" },
          items: [
            { nombre: "XX Lager", precio: 70 },
            { nombre: "XX Ámbar", precio: 70 },
            { nombre: "Sol", precio: 70 },
            { nombre: "Tecate Light", precio: 70 },
            { nombre: "Indio", precio: 70 },
            { nombre: "Chelada", precio: 80 },
            { nombre: "Michelada", precio: 90 },
            { nombre: "Ojo Rojo", precio: 100 },
          ],
        },
        {
          titulo: { es: "Refrescos y agua", en: "Sodas & water" },
          items: [
            { nombre: "Coca-Cola", precio: 50 },
            { nombre: "Coca-Cola Light", precio: 50 },
            { nombre: "Sprite", precio: 50 },
            { nombre: "Fanta", precio: 50 },
            { nombre: { es: "Agua mineral", en: "Sparkling water" }, precio: 50 },
            { nombre: { es: "Agua purificada 500 ml", en: "Bottled water 500 ml" }, precio: 30 },
            { nombre: { es: "Agua purificada 1 L", en: "Bottled water 1 L" }, precio: 40 },
          ],
        },
      ],
    },
  ],
};
