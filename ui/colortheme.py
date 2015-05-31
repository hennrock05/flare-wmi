from PyQt5.QtGui import QColor


class ColorTheme(object):
    """ interface """

    def get_accent(self, index):
        """
        :rtype: PyQt5.QtGui.QColor
        """
        raise NotImplementedError()


class LightPastelColorTheme(ColorTheme):
    """
    #####  Color Palette by Paletton.com
    #####  Palette URL: http://paletton.com/#uid=75a0u0kcglL4Zvw8Eq6eXhmkwen


    *** Primary color:

       shade 0 = #8B5674 = rgb(139, 86,116) = rgba(139, 86,116,1) = rgb0(0.545,0.337,0.455)
       shade 1 = #C9AABC = rgb(201,170,188) = rgba(201,170,188,1) = rgb0(0.788,0.667,0.737)
       shade 2 = #A77A93 = rgb(167,122,147) = rgba(167,122,147,1) = rgb0(0.655,0.478,0.576)
       shade 3 = #6F3B58 = rgb(111, 59, 88) = rgba(111, 59, 88,1) = rgb0(0.435,0.231,0.345)
       shade 4 = #5C2142 = rgb( 92, 33, 66) = rgba( 92, 33, 66,1) = rgb0(0.361,0.129,0.259)

    *** Secondary color (1):

       shade 0 = #AD6B6B = rgb(173,107,107) = rgba(173,107,107,1) = rgb0(0.678,0.42,0.42)
       shade 1 = #FBD4D4 = rgb(251,212,212) = rgba(251,212,212,1) = rgb0(0.984,0.831,0.831)
       shade 2 = #D09898 = rgb(208,152,152) = rgba(208,152,152,1) = rgb0(0.816,0.596,0.596)
       shade 3 = #8A4A4A = rgb(138, 74, 74) = rgba(138, 74, 74,1) = rgb0(0.541,0.29,0.29)
       shade 4 = #722929 = rgb(114, 41, 41) = rgba(114, 41, 41,1) = rgb0(0.447,0.161,0.161)

    *** Secondary color (2):

       shade 0 = #568B56 = rgb( 86,139, 86) = rgba( 86,139, 86,1) = rgb0(0.337,0.545,0.337)
       shade 1 = #AAC9AA = rgb(170,201,170) = rgba(170,201,170,1) = rgb0(0.667,0.788,0.667)
       shade 2 = #79A679 = rgb(121,166,121) = rgba(121,166,121,1) = rgb0(0.475,0.651,0.475)
       shade 3 = #3B6F3B = rgb( 59,111, 59) = rgba( 59,111, 59,1) = rgb0(0.231,0.435,0.231)
       shade 4 = #215C21 = rgb( 33, 92, 33) = rgba( 33, 92, 33,1) = rgb0(0.129,0.361,0.129)

    *** Complement color:

       shade 0 = #8DA264 = rgb(141,162,100) = rgba(141,162,100,1) = rgb0(0.553,0.635,0.392)
       shade 1 = #DEEAC6 = rgb(222,234,198) = rgba(222,234,198,1) = rgb0(0.871,0.918,0.776)
       shade 2 = #B1C28E = rgb(177,194,142) = rgba(177,194,142,1) = rgb0(0.694,0.761,0.557)
       shade 3 = #6D8145 = rgb(109,129, 69) = rgba(109,129, 69,1) = rgb0(0.427,0.506,0.271)
       shade 4 = #546B26 = rgb( 84,107, 38) = rgba( 84,107, 38,1) = rgb0(0.329,0.42,0.149)


    #####  Generated by Paletton.com (c) 2002-2014
    """
    COLORS = (
        QColor("#8B5674"),
        QColor("#AD6B6B"),
        QColor("#568B56"),
        QColor("#8DA264"),
    )

    @staticmethod
    def get_accent(index):
        # use .lighter() because colors don't seem to be matching expected colors (as seen on intertubes)
        #   and I know next to nothing about computers and colors.
        return LightPastelColorTheme.COLORS[index % len(LightPastelColorTheme.COLORS)].lighter()


class SolarizedColorTheme(ColorTheme):
    """
    via http://ethanschoonover.com/solarized
    solarized accent colors:

        $yellow:    #b58900;
        $orange:    #cb4b16;
        $red:       #dc322f;
        $magenta:   #d33682;
        $violet:    #6c71c4;
        $blue:      #268bd2;
        $cyan:      #2aa198;
        $green:     #859900;
    """
    COLORS = (
        QColor("#b58900"),
        QColor("#cb4b16"),
        QColor("#dc322f"),
        QColor("#d33682"),
        QColor("#6c71c4"),
        QColor("#268bd2"),
        QColor("#2aa198"),
        QColor("#859900"),
    )

    @staticmethod
    def get_accent(index):
        # use .lighter() because colors don't seem to be matching expected colors (as seen on intertubes)
        #   and I know next to nothing about computers and colors.
        return SolarizedColorTheme.COLORS[index % len(SolarizedColorTheme.COLORS)].lighter()