# iPadRestrictionsCodeBypass

This is a proof of concept script that was developed to highlight a security flaw in the latest and previous iOSs at the time of writing. (8.3)

iPads/iPhones can be hardened and this is especially useful when they are deployed in strict security organizations for 
business use. 

A common way to prevent the corporate iPad/iPhone user to access restricted features is to use a 4 digit pin restrictions code.

When one tries to bruteforce, a time delay takes place after few tries (ie: 1 hour delay until next try is possible). This control 
would effectively block brute force attempts if effective. 

However this control ban be bypassed and the pin code can be bruteforced in an automated manner by using an old hacking trick.

By using a lightning connector <-> mother usb port we connect a fake keyboard (in this case the Rubbery Ducky keystroke innjection
platform) to the iPad, and make use of the python script residing in this repository to generate the bruteforcing payload.

Please note this POC was purely done for informative purposes and was not quality tested or adjusted to work with all devices.

For video demo please see:

https://youtu.be/ceDA_4_omgw

