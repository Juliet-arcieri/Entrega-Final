# Casos de Prueba

## Caso de Prueba 1: Crear un Nuevo Blog
- **ID:** CP-01
- **Descripción:** Verificar que un usuario puede crear un nuevo blog.
- **Pasos para Ejecutar:**
  1. Iniciar sesión en la aplicación.
  2. Navegar a la página de añadir blog.
  3. Rellenar el formulario con un título, subtítulo, contenido, y una imagen.
  4. Hacer clic en "Guardar".
- **Datos de Prueba:** Título: "Mi Nuevo Blog", Subtítulo: "Subtítulo de Prueba", Contenido: "Contenido del blog", Imagen: [imagen.jpg].
- **Resultado Esperado:** El nuevo blog aparece en la lista de blogs con los detalles correctos.

## Caso de Prueba 2: Iniciar Sesión de Usuario
- **ID:** CP-02
- **Descripción:** Verificar que un usuario puede iniciar sesión.
- **Pasos para Ejecutar:**
  1. Navegar a la página de inicio de sesión.
  2. Ingresar nombre de usuario y contraseña.
  3. Hacer clic en "Iniciar sesión".
- **Datos de Prueba:** Nombre de Usuario: "usuario@ejemplo.com", Contraseña: "contraseña123".
- **Resultado Esperado:** El usuario es redirigido a la página de inicio con sesión iniciada.

## Caso de Prueba 3: Ver Blog Detalle
- **ID:** CP-03
- **Descripción:** Verificar que el detalle del blog se muestra correctamente.
- **Pasos para Ejecutar:**
  1. Navegar a la lista de blogs.
  2. Hacer clic en un blog para ver sus detalles.
- **Datos de Prueba:** Blog con ID 1.
- **Resultado Esperado:** La página de detalles del blog muestra el título, subtítulo, contenido y la imagen del blog correctamente.
