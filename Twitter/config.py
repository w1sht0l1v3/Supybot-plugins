###
# Copyright (c) 2011, Valentin Lorentz
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.conf as conf
import supybot.registry as registry

try:
    from supybot.i18n import PluginInternationalization
    from supybot.i18n import internationalizeDocstring
    _ = PluginInternationalization('Twitter')
except:
    # This are useless functions that's allow to run the plugin on a bot
    # without the i18n plugin
    _ = lambda x:x
    internationalizeDocstring = lambda x:x

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Twitter', True)


Twitter = conf.registerPlugin('Twitter')
# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(Twitter, 'someConfigVariableName',
#     registry.Boolean(False, _("""Help for someConfigVariableName.""")))
conf.registerGroup(Twitter, 'accounts')

helpGetToken = _('running get_access_token.py is a way to get it')

conf.registergroup(twitter, 'consumer')
conf.registerglobalvalue(twitter.consumer, 'key',
        registry.string('bItq1HZhBGyx5Y8ardIeQ',
            _("""The consumer key of the application.""")))
conf.registerglobalvalue(twitter.consumer, 'secret',
        registry.string('qjC6Ye6xSMM3XPLR3LLeMqOP4ri0rgoYFT2si1RpY',
            _("""The consumer secret of the application."""), private=true))

conf.registergroup(twitter.accounts, 'bot')
conf.registerglobalvalue(twitter.accounts.bot, 'key',
        registry.string('', _("""the twitter access token key for the bot's
        account (%s)""") % helpgettoken))
conf.registerglobalvalue(twitter.accounts.bot, 'secret',
        registry.string('', _("""the twitter access token secret for the bot's
        account (%s)""") % helpgettoken, private=true))
conf.registerGlobalValue(Twitter.accounts.bot, 'api',
        registry.String('https://api.twitter.com/1', _("""The URL to the
        base API URL (by default, it is Twitter.com, but you can use it
        for twitter-compatible services, such as identica/statusnet.""")))

conf.registerGroup(Twitter.accounts, 'channel')
conf.registerChannelValue(Twitter.accounts.channel, 'key',
        registry.String('', _("""The Twitter Access Token key for this
        channel's account (%s)""") % helpGetToken))
conf.registerChannelValue(Twitter.accounts.channel, 'secret',
        registry.String('', _("""The Twitter Access Token secret for this
        channel's account (%s)""") % helpGetToken, private=True))
conf.registerGlobalValue(Twitter.accounts.channel, 'api',
        registry.String('https://api.twitter.com/1', _("""The URL to the
        base API URL (by default, it is Twitter.com, but you can use it
        for twitter-compatible services, such as identica/statusnet.""")))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
