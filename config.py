import os
from typing import Optional, Literal

import pydantic
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

from browserstack_mobil.utils import path

EnvContext = Literal['remote', 'local']


class Settings(pydantic.BaseSettings):
    context: EnvContext = 'remote'
    load_dotenv()

    # Specify device and os_version
    platformName: str = None
    platformVersion: str = None
    deviceName: str = None
    app: Optional[str] = None
    appName: Optional[str] = None

    # BrowserStack capabilities
    projectName: Optional[str] = None
    buildName: Optional[str] = None
    sessionName: Optional[str] = None

    # Credentials
    if context == 'remote':
        userNam: Optional[str] = os.getenv('browserstack.userNam')
        accessKey: Optional[str] = os.getenv('browserstack.accessKey')
    else:
        userNam: Optional[str] = os.getenv('local.userNam')
        accessKey: Optional[str] = os.getenv('local.accessKey')

    # Remote Driver
    remote_url: str = 'http://hub.browserstack.com/wd/hub'

    # Selene
    timeout: float = 6.0

    @property
    def driver_options(self):
        options = UiAutomator2Options()
        options.device_name = self.deviceName
        options.platform_name = self.platformName
        options.app = self.app
        if 'hub.browserstack.com' in self.remote_url:
            options.load_capabilities(
                {
                    'platformVersion': self.platformVersion,
                    'bstack:options': {
                        'projectName': self.projectName,
                        'buildName': self.buildName,
                        'sessionName': self.sessionName,
                        'userName': self.userNam,
                        'accessKey': self.accessKey
                    }
                }
            )

        return options

    @classmethod
    def in_context(cls, env: Optional[EnvContext] = None) -> 'Settings':
        """
                factory method to init Settings with values from corresponding .env file
        """

        asked_or_current = env or cls().context
        return cls(
            _env_file=path.relative_from_root(f'.env.config.{asked_or_current}')
        )


# settings = Settings(_env_file=path.relative_from_root('.env.config.remote'))
settings = Settings.in_context()
