HexaCode API Reference
=======================

The HexaCode API allows you to execute HexaCode scripts programmatically.

Endpoint: `/api/execute`
------------------------

**Method**: POST  
**Request Body**:
- `script` (string): The HexaCode script to execute.

Example Request:
----------------

Send a request with the script to execute:

.. code-block:: json

    {
        "script": "AFFICHE \"Bonjour, API!\""
    }

Example Response:
-----------------

The API returns the output of the script:

.. code-block:: json

    {
        "output": "Bonjour, API!"
    }

Error Handling:
---------------

- **400**: Empty or invalid script provided.
- **500**: Internal server error.

