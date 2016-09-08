from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import register_setting


register_setting(
    name='FACEBOOK_APP_ID',
    label='Facebook App ID',
    description=_('Register an app at http://developers.facebook.com/'),
    editable=True,
    default="",
)

register_setting(
    name='FACEBOOK_APP_SECRET',
    label='Facebook App Secret',
    editable=True,
    default="",
)
