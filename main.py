import logging

# Dårlig praksis: Bruger basicConfig på en måde, der ikke differentierer mellem logniveauer
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(message)s')


def handle_request(user_id, request_data):
    # Potentielt følsom data logges
    logging.info(f"Handling request for user {user_id}: {request_data}")

    # Overlogging: Logger hver lille handling
    logging.debug("Checking user permissions")
    # Simulerer nogle operationer...
    logging.debug("User permissions verified")

    logging.debug("Processing request data")
    # Simulerer nogle operationer...
    logging.debug("Request data processed")

    try:
        # Simulerer en operation, der kan fejle
        result = "Operation successful"
        logging.info(f"Operation result for user {user_id}: {result}")
    except Exception as e:
        logging.error(f"Error during operation for user {user_id}: {e}")


def main():
    user_requests = [("user123", "{credit_card_number: '1234-5678-9012-3456', operation: 'purchase'}"),
                     ("user456", "{operation: 'check_balance'}")]

    for user_id, request_data in user_requests:
        handle_request(user_id, request_data)


if __name__ == "__main__":
    main()
