from marshmallow import Schema, fields, validate, EXCLUDE


class UserCreateSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    name = fields.String(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6))


class UserUpdateSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    name = fields.String(validate=validate.Length(min=3))
    email = fields.Email()
    password = fields.String(validate=validate.Length(min=6))
