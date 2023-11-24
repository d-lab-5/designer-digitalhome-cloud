Blockly.Blocks['start'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Project Start");
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField(new Blockly.FieldDropdown([["option","FR_NORME"], ["option","BE_NORME"], ["option","DE_NORME"]]), "NORME");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};