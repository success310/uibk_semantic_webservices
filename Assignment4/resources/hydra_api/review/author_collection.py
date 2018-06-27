from .. import collection_factory
from ..supportedProperty import HydraProperty, HydraPropertyInfo



author_class = collection_factory.create_collection(
      type_id = "vocab:AuthorCollection"
    , label = "AuthorCollection"
    , description = "A collection of authors"
    , entry_label = "author"
    , operation_prefix = "author"
    , end_point = "authors"
    , entry_point_name = "authors"
    , entry_context_name = "Author"
    , expects_type = "http://schema.org/Author"
    , returns_type = "http://schema.org/Author"
)


properties = []
properties.append(HydraProperty(
    title ="familyName",
    desc = "Family name of the author",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "http://schema.org/familyName"
    )
))
properties.append(HydraProperty(
    title ="givenName",
    desc = "First name of the author",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "http://schema.org/givenName"
    )
))
properties.append(HydraProperty(
    title ="email",
    desc = "email of the author",
    required = True,
    readonly = False,
    writeonly = False,
    property = HydraPropertyInfo(
        id = "http://schema.org/email"
    )
))

collection_factory.create_collection_entry(
    type_id = "http://schema.org/Author"
    , label = "Author"
    , description = "A author for a event"
    , hydra_title = "author"
    , operation_prefix = "author"
    , end_point = "authors"
    , properties = properties
)