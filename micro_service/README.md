Ideally this template should be used when breaking a monolith(created with base_service template) into multiple micro-services.

Params to be passed in CLI:

- service: The name of the project folder(default: example_service)
- create_db: Should a db folder along with alembic config be created(n for no, y for yes, default: y)
- create_ai: Should a folder with empty file `neural_net.py` be created(n for no, y for yes, default: y)
- create_proto: Should a folder with proto_files directory with `base.proto` be created(n for no, y for yes, default: y)
