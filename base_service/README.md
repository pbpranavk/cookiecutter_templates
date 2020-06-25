Ideally this template should be used at beginning of the lifecycle of product with all options answered with y. As gradually the product develops and gains traction, micro-services should be created from this(depending on the traffic to each module) and slowly it should gradually just become a gateway between frontend and micro-services.

Params to be passed in CLI:

- project_name : The name of the folder to be generated (default: base service)
- create_db: Should a db folder along with alembic config be created(n for no, y for yes, default: n)
- create_ai: Should a folder with empty file `neural_net.py` be created(n for no, y for yes, default: n)
- create_proto: Should a folder with proto_files directory with `base.proto` be created(n for no, y for yes, default: n)
