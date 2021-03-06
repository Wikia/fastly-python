A Python client library for Fastly
----------------------------------

www.fastly.com

Example:
~~~~~~~~

::

    import fastly

    # Connects to Fastly using API key.
    client = fastly.connect("your-api-key")

    # Need to fully authenticate to access all features. 
    client.login("email@domain.com", "h4x0rp4ssw0rd")

    # Get your account details.
    current_customer = client.get_current_customer()

    # Get your user details.
    current_user =  client.get_current_user()

    # List all services.
    all_services = client.list_services()

    # Create a service.
    service = client.create_service(current_customer.id,
        "test-service",
        comment="A service for testing out the client.")

    # Create a new version of the service.
    service_version = client.create_service_version(service.id,
        comment="A new version of this service.")

    # Create a domain.
    domain = client.create_domain(service.id, 
        service_version.number,
        "www.test.com",
        comment="A new domain.")

    # List domains associated with this version.
    print client.list_domains(service.id, service_version.number)

    # Delete the domain we just created.
    client.delete_domain(service.id, service_version.number, domain.name)
