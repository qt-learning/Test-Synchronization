import QtQuick
import QtQuick.Window
import QtQuick.Controls.Material

Window {
    id: root
    width: 640
    height: 480
    visible: true
    title: qsTr("Test Sync Example")

    Connections {
        target: myLoader.item

        function onUpdateStatus(status : string) : void {
            myStatus.text = status
            myLoader.sourceComponent = null
            openButton.enabled = true
        }
    }

    Column {
        anchors.centerIn: parent
        spacing: 10

        Text {
            id: myStatus
            anchors.horizontalCenter: parent.horizontalCenter
            font.pointSize: 16
            text: "Popup ready"
        }

        Row {
            anchors.horizontalCenter: parent.horizontalCenter
            spacing: 10

            Button {
                id: openButton
                height: 50
                width: 100
                text: "Open"

                onClicked: {
                    myStatus.text = "Popup opening..."
                    openButton.enabled = false
                    myLoader.visible = false
                    myLoader.sourceComponent = myComponent
                }
            }
        }

        Item {
            height: 100
            width: 200
            anchors.horizontalCenter: parent.horizontalCenter

            Loader {
                id: myLoader
                asynchronous: true
                visible: false

                onLoaded: {
                    visible = true
                    myStatus.text = "Popup opened"
                }
            }

            Component {
                id: myComponent

                Item {
                    id: rootItm
                    height: 100
                    width: 200

                    signal updateStatus(string status)

                    Repeater {
                        model: 5000

                        Rectangle {
                            id: myRect
                            anchors.fill: parent
                            color: "lightgreen"
                            border.color: "black"

                            Text {
                                anchors.centerIn: parent
                                text: "Popup"
                            }
                        }
                    }

                    Button {
                        id: closeButton
                        anchors.centerIn: parent
                        height: 100
                        width: 175
                        text: "Click to close"

                        onClicked: {
                            rootItm.updateStatus("Popup closed")
                        }
                    }
                }
            }
        }
    }
}
