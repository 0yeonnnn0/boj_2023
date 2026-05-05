class Solution {
    fun solution(citations: IntArray): Int {
        
        val des_citations = citations.sortedDescending()
        var h_index = 0
        
        for (i in des_citations.indices) {
            if(des_citations[i] >= i + 1) {
                h_index = i + 1
            } else {
                break
            }
        }       
        return h_index
    }    
}