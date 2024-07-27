# API Specification

## Overview
The Advanced Phishing Detection Tool does not currently provide an API interface. However, future versions may include a RESTful API for integrating with other systems.

## Proposed Endpoints
  - POST /predict: Predicts whether the provided content or URL is phishing.
  - Request Body: JSON containing the content or URL.
  - Response: JSON with the prediction result (phishing or legitimate).

## Example Request
 json
{
  "content": "Your account has been suspended. Click here to reactivate."
}
