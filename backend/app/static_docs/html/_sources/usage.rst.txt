Using the HexaCode Playground
=============================

The HexaCode Playground is a web-based environment where you can write and execute HexaCode scripts without downloads.

Steps to Use:
-------------

1. Open the HexaCode Playground in your browser.
2. Write your code in the **Editor** section.
3. Click the **Run** button to execute your code.
4. View the output in the **Console** section.

Example Workflow:
-----------------

Write this simple script in the editor:

.. code-block:: hexacode

    AFFICHE "Bienvenue au HexaCode Playground!"

Click **Run**, and you'll see:

.. code-block:: text

    Bienvenue au HexaCode Playground!

Supported Commands:
-------------------

- **AFFICHE**: Print a message to the console.
  Example:
  .. code-block:: hexacode

      AFFICHE "Ceci est un test."

- **SI**: Conditional statements.
  Example:
  .. code-block:: hexacode

      SI 5 > 3 ALORS
          AFFICHE "Vrai!"
      SINON
          AFFICHE "Faux!"
