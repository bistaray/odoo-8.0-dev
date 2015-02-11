XML needs to be added manually:

<xpath expr="//div[@name='buttons']" position="after">

                        <button class="oe_inline oe_stat_button" name="attachment_tree_view"  type="object" icon="fa-files-o">
                            <field string="Documents" name="doc_count" widget="statinfo"/>
                        </button>

</xpath>
