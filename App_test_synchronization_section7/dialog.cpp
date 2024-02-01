#include "dialog.h"
#include "ui_dialog.h"
#include <QThread>

Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Dialog)
{
    ui->setupUi(this);
}

Dialog::~Dialog()
{
    delete ui;
}

void Dialog::on_closeDialogBtn_clicked()
{
    accept();
}

