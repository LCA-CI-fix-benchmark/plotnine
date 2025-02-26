from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .doc import RenderDoc
from .mixin_call import RenderDocCallMixin
from .mixin_members import RenderDocMembersMixin

if TYPE_CHECKING:
    from griffe import dataclasses as dc
    from quartodoc import layout


@dataclass
class __RenderDocClass(RenderDocMembersMixin, RenderDocCallMixin, RenderDoc):
    """
    Render documentation for a class (layout.DocClass)
    """

    def __post_init__(self):
        super().__post_init__()
        # We narrow the type with a TypeAlias since we do not expect
        # any subclasses to have narrower types
        self.doc: layout.DocClass = self.doc
        self.obj: dc.Class = self.obj


class RenderDocClass(__RenderDocClass):
    """
    Extend Rendering of a layout.DocClass object
    """
